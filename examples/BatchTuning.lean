import Std

namespace BatchTuning
inductive Size where | one | two | four | eight deriving DecidableEq, Repr
open Size
def width : Size → Nat | one => 1 | two => 2 | four => 4 | eight => 8
def options := [one,two,four,eight]
def calls (s : Size) := 8 / width s
def feasible (limit s : Size) := decide (width s ≤ width limit)
def next : Size → Size | one => two | two => four | four => eight | eight => eight
def step (limit s : Size) :=
  let q := next s
  if feasible limit q && decide (calls q < calls s) then q else s
def loop (limit : Size) (pin : Size) : Nat → Size
  | 0 => pin
  | n+1 => step limit (loop limit pin n)

-- The equivalence class contains exactly four divisors of the eight-record workload.
-- At every accepted pin the same latency contract is reapplied.
theorem one_step (limit s : Size) (ok : feasible limit s = true) :
    feasible limit (step limit s) = true ∧ calls (step limit s) ≤ calls s := by
  revert ok; cases limit <;> cases s <;> decide

theorem fixed_optimum (limit start : Size) (ok : feasible limit start = true) :
    let winner := loop limit start 3
    feasible limit winner = true ∧ step limit winner = winner ∧
    ∀ q, feasible limit q = true → calls winner ≤ calls q := by
  intro winner
  refine ⟨?_, ?_, ?_⟩
  · revert ok; cases limit <;> cases start <;> decide
  · revert ok; cases limit <;> cases start <;> decide
  · intro q; revert ok; cases limit <;> cases start <;> cases q <;> decide

def trace := (List.range 4).map (fun n => loop four one n)
theorem before_after : trace = [one,two,four,four] ∧ calls one = 8 ∧ calls four = 2 ∧
    calls eight = 1 ∧ feasible four eight = false ∧ feasible two four = false := by decide

#eval (trace, trace.map calls)
#print axioms one_step
#print axioms fixed_optimum
#print axioms before_after
end BatchTuning
