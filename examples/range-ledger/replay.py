"""Build real SQLite receipts from one streaming pass; compare scoped release answers."""
import json
import sqlite3
import tempfile
from pathlib import Path

BANKS = ((0, 1024), (1024, 2048), (2048, 3072), (3072, 4096))
OVERLAP = ((0, 3072), (1024, 3072), (1024, 4096))
SIXTY_FOURS = tuple((i, i + 64) for i in range(0, 512, 64))


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def scan(db):
    result = [value for value, in db.execute("SELECT value FROM samples ORDER BY id")]
    require(len(result) == 4096, "incomplete source snapshot")
    return result


def build(db, epoch, layouts, include_potentials=False):
    values = scan(db)
    prefix = [0]
    for value in values:
        prefix.append(prefix[-1] + value)
    written = 0
    for layout, spans in layouts:
        rows = [(epoch, layout, a, b, prefix[b] - prefix[a]) for a, b in spans]
        db.executemany("INSERT INTO receipts VALUES (?,?,?,?,?)", rows)
        written += len(rows)
    if include_potentials:
        db.executemany("INSERT INTO potentials VALUES (?,?,?)",
                       ((epoch, k, prefix[k]) for k in (0, 4096)))
        written += 2
    return len(values), written


def read(db, epoch, layout, spans):
    values = []
    for a, b in spans:
        row = db.execute("SELECT value FROM receipts WHERE epoch=? AND layout=? AND a=? AND b=?",
                         (epoch, layout, a, b)).fetchone()
        if row is None:
            raise ValueError("receipt unavailable for this epoch/layout")
        values.append(row[0])
    return values


def query(db, epoch):
    raw = scan(db)
    banks = read(db, epoch, "banks", BANKS)
    overlaps = read(db, epoch, "overlap", OVERLAP)
    x, y, z = overlaps
    ends = dict(db.execute("SELECT endpoint,value FROM potentials WHERE epoch=?", (epoch,)))
    require(set(ends) == {0, 4096}, "incomplete potential venue")
    direct = sum(raw)
    require(direct == sum(banks) == x-y+z == ends[4096]-ends[0], "venue disagreement")
    require(direct == db.execute("SELECT SUM(value) FROM samples").fetchone()[0], "SQL disagreement")
    return direct, {"raw":len(raw), "banks":len(banks), "overlap":len(overlaps), "prefix":len(ends)}


def verify():
    with tempfile.TemporaryDirectory() as temp, sqlite3.connect(Path(temp)/"readings.sqlite") as db:
        db.executescript("""
        CREATE TABLE samples(id INTEGER PRIMARY KEY, value INTEGER NOT NULL);
        CREATE TABLE receipts(epoch, layout, a, b, value INTEGER NOT NULL, PRIMARY KEY(epoch,layout,a,b));
        CREATE TABLE potentials(epoch, endpoint, value INTEGER NOT NULL, PRIMARY KEY(epoch,endpoint));
        """)
        db.executemany("INSERT INTO samples VALUES (?,?)",
                       ((i, (i*37 + i//11) % 257 - 125) for i in range(4096)))
        layouts = (("banks",BANKS), ("overlap",OVERLAP), ("tiles",SIXTY_FOURS))
        require(build(db, 0, layouts, True)[0] == 4096, "bad build count")
        old, counts = query(db, 0)
        source_reads, receipt_writes = build(db, "standalone", (("overlap", OVERLAP),))
        raw_reads = receipt_reads = 0
        for _ in range(2):
            cells = scan(db)
            scalars = read(db, "standalone", "overlap", OVERLAP)
            require(sum(cells) == scalars[0]-scalars[1]+scalars[2], "standalone result mismatch")
            raw_reads += len(cells)
            receipt_reads += len(scalars)
        charged = source_reads + receipt_writes + receipt_reads
        require((raw_reads, charged) == (8192, 4105), "index construction accounting mismatch")
        old_tiles = read(db, 0, "tiles", SIXTY_FOURS)
        for i, change in ((100, 7), (200, -7)):
            db.execute("UPDATE samples SET value=value+? WHERE id=?", (change, i))
        build(db, 1, layouts, True)
        new, counts1 = query(db, 1)
        current_tiles = read(db, 1, "tiles", SIXTY_FOURS)
        changed = [span for span, a, b in zip(SIXTY_FOURS, old_tiles, current_tiles) if a != b]
        require(changed == [(64,128),(192,256)] and new == old, "cancellation failed")
        db.execute("UPDATE samples SET value=value+1 WHERE id=2050")
        build(db, 2, layouts, True)
        latest, counts2 = query(db, 2)
        require(counts == counts1 == counts2, "query scope changed")
        require(latest == new+1, "stale final total accepted")
        try:
            read(db, 3, "overlap", OVERLAP)
        except ValueError:
            pass
        else:
            raise RuntimeError("missing epoch accepted")
        receipt = {"sqlite": sqlite3.sqlite_version, "epoch_totals": [old,new,latest],
                   "query_rows": counts,
                   "stale_tiles": changed,
                   "overlap_index_two_queries": {"raw_rows":raw_reads, "reads_plus_writes":charged}}
        print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    verify()
