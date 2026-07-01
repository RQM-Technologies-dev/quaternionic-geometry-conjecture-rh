# Weil Explicit-Formula Bridge

This note records the next proof direction after the Candidate v0 Lemma A
construction and Lemma B proof. It studies Lemma C through the classical route
emphasized in Bombieri's Millennium problem article: Weil's explicit formula,
positivity, and the search for an index-theorem analogue.

This is a bridge audit, not a proof of the Riemann Hypothesis.

Local source copy:
[bombieri-riemann-hypothesis-millennium.pdf](../references/bombieri-riemann-hypothesis-millennium.pdf).

## Original Problem Anchor

Bombieri's account frames the Riemann Hypothesis as a statement about the
location of the nontrivial zeros of `zeta(s)`, but it also points to the deeper
proof mechanism suggested by the known analogues:

- Riemann's explicit formula links primes and zeros.
- Weil's explicit formula recasts RH as a sign condition for a class of test
  functions.
- In the finite-field case, the analogous sign condition is supplied by an
  index theorem and cohomological structure.
- The missing classical mechanism is an analogue of that positivity or
  index-theorem structure.

For this repository, the important consequence is that Lemma C should not be
treated as a formal consequence of completed symmetry alone.

## Current Candidate v0 Position

Candidate v0 now has:

```text
Lemma A: theta kernel -> Phi_Xi -> mu_Xi
Lemma B: S_Xi(s)=0 iff Re(s)=1/2
```

The remaining theorem-level bridge is:

```text
Lemma C: Xi(s)=0 => S_Xi(s)=0.
```

Lemma B proves that scale-stability forces the critical line. It does not prove
that zeros are scale-stable.

The obstruction is structural. Candidate v0 writes

```text
s = 1/2 + alpha + i t
```

and measures the real scale tilt through

```text
M(alpha) M(-alpha) >= 1.
```

Zeros of `Xi(1/2 + alpha + i t)` are oscillatory cancellations in `t`. The
Candidate v0 defect detects `alpha`. A bridge theorem must explain why a zero
forces equality in the Candidate v0 Cauchy-Schwarz inequality.

## Weil-Bridge Target

The next serious target is to connect Candidate v0 to a Weil-type quadratic
form. In Bombieri's convention, RH is equivalent to a sign condition in the
explicit formula for test functions of the form

```text
f(x) = integral_0^infinity g(x y) g(y) dy,
```

with the normalization constraints

```text
integral_0^infinity g(x) dx / x = 0,
integral_0^infinity g(x) dx = 0.
```

The precise sign depends on the chosen explicit-formula convention. This repo
should keep Bombieri's sign convention when transcribing that formula.

The intended bridge shape is:

```text
Candidate v0 defect
  -> an admissible Weil test function or quadratic form
  -> explicit-formula sign condition
  -> off-line zeros violate the sign condition
  -> Xi(s)=0 forces S_Xi(s)=0.
```

## Required Work

1. Transcribe the exact Weil explicit formula in this repo's notation.

   The transcription must specify the Mellin transform convention, zero-sum
   convention, prime/local terms, archimedean terms, and sign convention.

2. Define an admissible test family tied to Candidate v0.

   The family should be derived from the theta-kernel measure `mu_Xi`, mirror
   scale profiles, or a controlled deformation of them. It must satisfy the
   test-function hypotheses before zero data is used.

3. Express the Candidate v0 defect inside the explicit-formula framework.

   The goal is not merely to compare formulas. The goal is to show that
   `S_Xi(s)` or a strengthened defect is represented by, bounded by, or
   equivalent to a Weil quadratic form.

4. Prove a sign theorem.

   A successful route must establish the needed positivity or negativity for the
   admissible test family without assuming RH and without tuning to known zero
   ordinates.

5. Derive Lemma C.

   Only after the sign theorem is available can the repo attempt the implication

   ```text
   Xi(s)=0 => S_Xi(s)=0.
   ```

## Failure Mode To Watch

Candidate v0 may be only an axis detector. If no non-circular Weil quadratic
form can be attached to `S_Xi`, then Candidate v0 should remain as Lemma A/B
scaffolding and the proof route should be strengthened.

The likely strengthening would add an explicit-formula energy term that sees
both:

```text
scale imbalance alpha,
oscillatory cancellation at height t.
```

That would make the proof target:

```text
Xi(s)=0
  -> zero-energy or extremal condition in a Weil-positive form
  -> alpha=0.
```

## Active Transcription Note

The precise transcription is:

```text
docs/08_weil_formula_transcription.md
```

It locks the explicit formula, test-function class, sign convention,
normalization constraints, and Candidate v0 attachment test needed before any
new Lemma C theory is introduced.
