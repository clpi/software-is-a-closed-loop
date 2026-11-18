import Identifiable
import AdaptiveReads
import OverlapPlan
import SignedStitch
import CertificateReuse
import LinearProvenance
import IntervalBasis

namespace RangeLedger.Settlement
open SignedStitch

def page (a b : Nat) (v : Int) : Receipt := ⟨a,b,v⟩
def leftPage (p : Nat → Int) := page 0 3072 (OverlapPlan.read p .left)
def midPage (p : Nat → Int) := page 1024 3072 (OverlapPlan.read p .overlap)
def rightPage (p : Nat → Int) := page 1024 4096 (OverlapPlan.read p .right)

-- Query the stored values. Check the matching seams while reversing the overlap.
def publish (l m r : Receipt) := chain l [rev m,r]
theorem publish_exact (p : Nat → Int) :
    publish (leftPage p) (midPage p) (rightPage p) = some (page 0 4096 (p 4096 - p 0)) := by
  change some (page 0 4096 (OverlapPlan.solve (OverlapPlan.read p .left)
    (OverlapPlan.read p .overlap) (OverlapPlan.read p .right))) = _
  rw [OverlapPlan.reconstruction]

-- The stored records can come from any producer. Their individual validity is
-- the trust boundary. Each start/stop is checked by the receiving contract.
theorem external_publish (p : Nat → Int) (x y z : Int)
    (hx : valid p (page 0 3072 x)) (hy : valid p (page 1024 3072 y))
    (hz : valid p (page 1024 4096 z)) :
    publish (page 0 3072 x) (page 1024 3072 y) (page 1024 4096 z) =
      some (page 0 4096 (LinearProvenance.eval p LinearProvenance.folded)) := by
  change x = p 3072 - p 0 at hx
  change y = p 3072 - p 1024 at hy
  change z = p 4096 - p 1024 at hz
  subst x; subst y; subst z
  exact publish_exact p

-- Old-vs-new output reuse is exact even when intermediate receipts change.
theorem release_reuse (p d : Nat → Int) :
    publish (leftPage (CertificateReuse.update p d)) (midPage (CertificateReuse.update p d))
      (rightPage (CertificateReuse.update p d)) =
      publish (leftPage p) (midPage p) (rightPage p) ↔ d 0 = d 4096 := by
  rw [publish_exact,publish_exact]
  change some (Receipt.mk 0 4096 _) = some (Receipt.mk 0 4096 _) ↔ _
  simpa only [Option.some.injEq,Receipt.mk.injEq,true_and] using
    (CertificateReuse.exact_reuse p d 0 4096)

def catalog (u v : Nat) := (u = 0 ∧ v = 3072) ∨ (u = 1024 ∧ v = 3072) ∨ (u = 1024 ∧ v = 4096)

theorem ledger_determines (p q : Nat → Int) (same : Identifiable.agrees catalog p q) :
    Identifiable.total p 0 4096 = Identifiable.total q 0 4096 := by
  apply (Identifiable.determined_iff catalog 0 4096).mpr _ p q same
  apply Identifiable.Path.join (b := 1024)
  · exact (Identifiable.Path.edge (Or.inl ⟨rfl,rfl⟩)).join
      (.reverse (.edge (Or.inr (Or.inl ⟨rfl,rfl⟩))))
  · exact .edge (Or.inr (Or.inr ⟨rfl,rfl⟩))

-- The four-bank optimum is a different read venue over the identical world.
theorem bank_venue (p : Nat → Int) (s : AdaptiveReads.Plan) (ok : AdaptiveReads.correct s) :
    (AdaptiveReads.run p AdaptiveReads.four).1 = LinearProvenance.eval p LinearProvenance.folded ∧
    (AdaptiveReads.run p AdaptiveReads.four).2.length ≤ (AdaptiveReads.run p s).2.length := by
  exact ⟨(AdaptiveReads.attains p).1, (AdaptiveReads.attains p).2 ▸ AdaptiveReads.lower_bound s ok p⟩

theorem overlap_is_essential (missing : OverlapPlan.Page) :
    (∀ j, j ≠ missing → OverlapPlan.read (fun _ => 0) j = OverlapPlan.read (OverlapPlan.other missing) j) ∧
    OverlapPlan.other missing 4096 - OverlapPlan.other missing 0 ≠ 0 := OverlapPlan.essential missing

-- A certified-additive implementation agreeing on unit samples returns the
-- same full-window value as the signed receipt publisher.
theorem validate_implementation (p : Nat → Int) (f : IntervalBasis.Answer)
    (shape : IntervalBasis.additive f) (units : IntervalBasis.singletons 4096 f (Identifiable.total p)) :
    publish (leftPage p) (midPage p) (rightPage p) = some (page 0 4096 (f 0 4096)) := by
  have sums : IntervalBasis.additive (Identifiable.total p) := by
    intro a b c _ _; unfold Identifiable.total; omega
  have eq := IntervalBasis.all_queries shape sums units 0 4095 (by decide)
  rw [publish_exact]; exact congrArg (fun v => some (page 0 4096 v)) eq.symm

-- Equal unit weights for source row reads, receipt writes, and receipt reads.
-- The index is built once; each query is a fresh reader with no answer cache.
theorem build_amortization (queries : Nat) :
    4096 + 3 + 3*queries < 4096*queries ↔ 2 ≤ queries := by omega

#print axioms validate_implementation
#print axioms build_amortization
#print axioms external_publish
#print axioms release_reuse
#print axioms ledger_determines
#print axioms bank_venue
#print axioms overlap_is_essential
end RangeLedger.Settlement
