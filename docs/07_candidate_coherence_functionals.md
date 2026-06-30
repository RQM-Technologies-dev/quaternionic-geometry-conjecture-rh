# Candidate Coherence Functionals

This document records three candidate versions of the spectral-coherence
functional

```text
C(q)
```

ranked from safest to boldest. Each candidate is a research object, not a
completed theorem. The goal is to move from a schematic coherence target to
testable mathematical objects with visible analytic obligations.

The current modeling defaults for domains, projections, conjugations,
normalization, and norm choices are recorded in the
[Definition Ledger](08_definition_ledger.md).

## Ranking

The candidates are:

1. `C_1(q)` - slice-restricted completed-zeta defect.
2. `C_2(q)` - Gamma-lift conjugacy defect.
3. `C_3(q)` - Weil/explicit-formula-inspired energy functional.

The first candidate is the safest because it stays closest to established
classical zeta theory. The third is the boldest because it tries to connect the
quaternionic model to positivity or coercivity structures related to known
analytic equivalents of the Riemann Hypothesis.

## 1. Slice-Restricted Completed-Zeta Defect

Choose a unit imaginary quaternion `u` and restrict to the complex slice

```text
q = a + t u.
```

Identify this slice with the complex variable

```text
s = a + i t.
```

Let `Xi(s)` denote a completed-zeta normalization satisfying the classical
functional symmetry

```text
Xi(s) = Xi(1-s).
```

The safest candidate begins with the slice residual

```text
C_1(q; u) = |Xi(s(q,u)) - Xi(1-s(q,u))|^2.
```

### What It Tests

This candidate tests whether the chosen slice projection, normalization, and
reflection convention reproduce the classical `s <-> 1-s` symmetry.

### Required Inputs

- a completed-zeta normalization `Xi(s)`,
- a slice choice `u`,
- a projection rule from `q = a + t u` to `s = a + i t`,
- a reflection convention for `s <-> 1-s`.

### Known Limitations

If `Xi(s)` is the exact classical completed zeta function, the residual is
zero by the functional equation. Therefore `C_1(q)` is mainly a baseline and
normalization check. By itself it does not identify zeros, define a
quaternionic lift, or supply off-slice control.

### Theorem-Level Obligations

Before this candidate can carry proof weight, the program would need to show
how a nontrivial coherence condition is extracted from the classical symmetry
without making the argument circular.

## 2. Gamma-Lift Conjugacy Defect

The intermediate candidate uses the quaternionic Gamma-lift target

```text
Gamma_H(q) = integral_0^infinity exp(-x) exp(q log x) dx.
```

A first conjugacy residual is

```text
C_2(q) = ||Gamma_H(conj(q)) - conj(Gamma_H(q))||^2.
```

This expression is only a candidate form. Its meaning depends on the future
choice of quaternionic domain, branch conventions, norm, and functional
calculus.

### What It Tests

This candidate tests whether the proposed Gamma lift respects quaternionic
conjugation in a way compatible with the classical Gamma factors inside the
completed zeta function.

### Required Inputs

- a precise domain for `Gamma_H(q)`,
- branch choices for logarithmic terms,
- a slice-regular or slice-compatible construction,
- a quaternionic norm,
- a multiplication-order convention.

### Known Limitations

The defect may vanish for formal or representation-theoretic reasons before it
captures any zeta-zero structure. It also does not yet include the zeta factor,
the powers of pi, or the full completed-zeta normalization.

### Theorem-Level Obligations

Before this candidate can carry proof weight, the program would need to
construct `Gamma_H(q)` rigorously and prove that its conjugacy behavior matches
the classical functional equation on every admissible slice.

## 3. Weil/Explicit-Formula-Inspired Energy Functional

The boldest candidate treats `C(q)` as an energy functional modeled on the
explicit formula and Weil-type positivity criteria.

The schematic target is

```text
C_3(q) = E_Weil(phi_q) + lift_defect(q) + slice_defect(q),
```

where `phi_q` is a test object derived from the quaternionic state, `E_Weil`
is an explicit-formula-inspired quadratic or energy term, and the remaining
terms record compatibility with the Gamma lift and critical-slice projection.

### What It Tests

This candidate tests whether the quaternionic coherence model can be connected
to positivity, negativity, or coercive behavior of the type that appears in
known analytic criteria related to the Riemann Hypothesis.

### Required Inputs

- a class of admissible test objects `phi_q`,
- an explicit-formula normalization,
- a rule connecting quaternionic states to test objects,
- a coercive or sign-definite structure,
- compatibility terms for the Gamma lift and slice projection.

### Known Limitations

This is the least immediate candidate because it requires the most analytic
infrastructure. It should not be presented as a proof strategy until the test
class, energy term, and coercivity statement are all stated precisely.

### Theorem-Level Obligations

Before this candidate can carry proof weight, the program would need to prove
that the quaternionic energy is equivalent to, or rigorously implies, a known
classical positivity criterion. This is the serious long-term target because
positivity and coercivity are where the Riemann Hypothesis has established
analytic equivalent forms.

## Working Interpretation

Use the candidates in order:

- `C_1(q)` as the classical normalization baseline,
- `C_2(q)` as the quaternionic lift and conjugacy diagnostic,
- `C_3(q)` as the long-term analytic target.

The development path should keep diagnostic agreement separate from theorem
claims. A candidate becomes mathematically significant only when its domain,
regularity, symmetry, stationarity, and off-slice control are stated without
circular dependence on the desired zero locations.
