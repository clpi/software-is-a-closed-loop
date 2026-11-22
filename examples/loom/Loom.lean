namespace Loom

-- A loom pattern is one derivation from a contract value to its figures.
-- The ledger row, the harness, and the held-out set are three readings of
-- that one derivation, so they agree by construction: the row states the
-- derived figure, the harness accepts exactly the derived figure, and a
-- held-out case is the same derivation at a fresh contract value.
structure Pattern (O F : Type) where
  derive : O → F

def row (p : Pattern O F) (o : O) : F :=
  p.derive o

def sample (p : Pattern O F) (o : O) : F :=
  p.derive o

def accepts (p : Pattern O F) (o : O) (stated : F) : Prop :=
  stated = p.derive o

-- The generated row always passes the generated harness.
theorem agrees (p : Pattern O F) (o : O) : accepts p o (row p o) :=
  rfl

-- A figure that differs from the derivation is refused: drift between a
-- stated row and its contract is exactly a refused figure.
theorem refuses (p : Pattern O F) (o : O) {stated : F} (h : stated ≠ p.derive o) :
    ¬ accepts p o stated :=
  h

-- A held-out case states the same figure the row states at that value.
theorem sampled (p : Pattern O F) (o : O) : sample p o = row p o :=
  rfl

-- The dense matrix multiply rate bar as a pattern over the incumbent
-- floor: one and a half times the floor, rounded half up at integer
-- precision. The generated row at the recorded floor of 431 is 647.
def gemm : Pattern Nat Nat where
  derive floor := (floor * 3 + 1) / 2

-- The call-cost bar in hundredths of a nanosecond: half the recorded
-- cost, rounded half up. The generated row at 73 is 37.
def call : Pattern Nat Nat where
  derive cost := (cost + 1) / 2

theorem bar : row gemm 431 = 647 :=
  rfl

theorem miss : ¬ accepts gemm 431 646 :=
  refuses gemm 431 (by decide)

theorem half : row call 73 = 37 :=
  rfl

end Loom

#print axioms Loom.agrees
#print axioms Loom.refuses
#print axioms Loom.sampled
#print axioms Loom.bar
#print axioms Loom.miss
#print axioms Loom.half
