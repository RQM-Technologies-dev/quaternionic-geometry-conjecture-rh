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

1. `C_1(q; u)` - slice-restricted completed-zeta defect.
2. `C_2(q)` - Gamma-lift conjugacy defect.
3. `C_3(q)` - Weil/explicit-formula-inspired energy functional.

The first candidate is the safest because it stays closest to established
classical zeta theory. The second candidate tests the quaternionic lift itself.
The third is the boldest because it tries to connect the quaternionic model to
positivity or coercivity structures related to known analytic equivalents of
the Riemann Hypothesis.

## 1. Slice-Restricted Completed-Zeta Defect

The first candidate is a baseline symmetry and normalization test on a fixed
complex slice. Choose an admissible unit imaginary quaternion `u`, restrict to

```text
q in L_u = {a + t u : a,t in R},
```

and project by

```text
s = pi_u(q) = a + i t.
```

Let the functional-equation reflection be

```text
R(s) = 1-s.
```

Using the completed-zeta normalization from the definition ledger,

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s),
```

the slice defect is

```text
D_1(q; u) = Xi(s) - Xi(R(s)).
```

The candidate functional is

```text
C_1(q; u) = |D_1(q; u)|^2.
```

### What It Tests

`C_1(q; u)` tests whether the slice projection, completed-zeta normalization,
and reflection convention reproduce the classical `s <-> 1-s` symmetry.

It can test:

- whether `pi_u(q)` is implemented consistently on each selected slice,
- whether the chosen `Xi(s)` normalization includes the correct Gamma and
  power-of-pi factors,
- whether the reflection used in diagnostics is `R(s)=1-s`,
- whether future numerical scripts produce residuals consistent with the
  classical functional equation.

### What It Does Not Test

If `Xi(s)` is the exact classical completed zeta function, then

```text
D_1(q; u) = 0
```

by the classical functional equation. Therefore `C_1(q; u)` is not a zero
detector by itself. It does not define a quaternionic lift, establish
stationarity, or supply off-slice control.

### Required Inputs

- a completed-zeta normalization `Xi(s)`,
- a slice choice `u`,
- the projection `pi_u(q)`,
- the reflection `R(s)=1-s`,
- a complex absolute value for the projected residual.

### Failure Modes

- A wrong completed-zeta normalization may create artificial residuals.
- A wrong projection convention may make slice comparisons meaningless.
- A numerical implementation may mistake roundoff or truncation error for a
  mathematical defect.
- Exact vanishing of the residual may be misread as evidence about zeros,
  rather than as a check of classical symmetry.

### Theorem-Level Obligations

Before this candidate can carry proof weight, the program would need to show
how a nontrivial coherence condition is extracted from the classical symmetry
without making the argument circular. In particular, any stationarity or
zero-location claim must be stated independently of known zero data.

## 2. Gamma-Lift Conjugacy Defect

The second candidate tests whether a quaternionic Gamma-lift respects the
selected quaternionic conjugation. It uses the guiding Gamma-lift target

```text
Gamma_H(q) = integral_0^infinity exp(-x) exp(q log x) dx.
```

Using the ledger notation `conj_H`, define the conjugacy defect

```text
D_2(q) = Gamma_H(conj_H(q)) - conj_H(Gamma_H(q)).
```

With the Euclidean quaternion norm

```text
||r + x i + y j + z k|| = sqrt(r^2 + x^2 + y^2 + z^2),
```

the candidate functional is

```text
C_2(q) = ||D_2(q)||^2.
```

### What It Tests

`C_2(q)` tests whether the proposed Gamma lift is compatible with quaternionic
conjugation in the sense required by the spectral-coherence model.

On a fixed admissible slice `L_u`, the expected minimum standard is
slice-compatibility: after domain and branch choices are fixed,
`Gamma_H(a + t u)` should reduce to the corresponding complex Gamma
continuation. Off-slice, `Gamma_H(q)` remains conjectural until the program
fixes a quaternionic functional calculus.

### Required Inputs

- a precise domain for `Gamma_H(q)`,
- excluded points or singular loci,
- branch choices for logarithmic terms,
- a slice-regular or slice-compatible construction,
- a multiplication-order convention,
- the Euclidean quaternion norm from the definition ledger,
- a clear distinction between slice-compatible behavior and off-slice
  conjectural behavior.

### Diagnostic Uses

`C_2(q)` can become useful as a diagnostic once `Gamma_H(q)` is implemented on
a specified domain. It can track:

- whether conjugate inputs produce conjugate Gamma-lift outputs,
- whether branch choices create discontinuities or artificial defects,
- whether defects concentrate away from the critical slice,
- whether the Gamma part of a future completed-zeta lift is internally
  consistent.

### Failure Modes

- The defect may vanish for formal reasons without encoding any zeta-zero
  structure.
- A branch convention may create artifacts that look like coherence defects.
- A chosen functional calculus may make `Gamma_H(q)` well-defined but
  unrelated to the classical zeta functional equation.
- The defect may only test Gamma-lift symmetry and never interact with the
  zeta factor, powers of pi, or completed-zeta normalization.

### Theorem-Level Obligations

Before this candidate can carry proof weight, the program would need to
construct `Gamma_H(q)` rigorously and prove that its conjugacy behavior matches
the classical Gamma factors on every admissible slice. It would also need to
show how the Gamma-lift defect enters a full completed-zeta or coherence
functional without depending on known zero locations.

## 3. Weil/Explicit-Formula-Inspired Energy Functional

The third candidate treats `C(q)` as an energy functional modeled on the
explicit formula and Weil-type positivity criteria. This is the serious
long-term candidate because positivity and coercivity are where the Riemann
Hypothesis has established analytic equivalent forms.

The schematic target is

```text
C_3(q) = E_Weil(phi_q) + lift_defect(q) + slice_defect(q).
```

The terms have different roles:

- `phi_q` is a test object derived from the quaternionic state `q`.
- `E_Weil(phi_q)` is an explicit-formula-inspired quadratic or energy term.
- `lift_defect(q)` records compatibility with the Gamma lift and other
  normalization choices.
- `slice_defect(q)` records departure from the projected critical-slice
  structure.

### What It Tests

`C_3(q)` tests whether the quaternionic coherence model can be connected to a
sign-definite or coercive analytic structure. Unlike `C_1(q; u)`, it is not
only a symmetry residual. Unlike `C_2(q)`, it is not only a Gamma-lift
conjugacy diagnostic. Its intended role is to become the bridge between the
geometric model and known explicit-formula or positivity criteria.

### Required Inputs

- a class of admissible test objects `phi_q`,
- a rule assigning `phi_q` to a quaternionic state `q`,
- an explicit-formula normalization,
- a candidate quadratic, energy, or pairing `E_Weil`,
- a sign, positivity, or coercivity target,
- compatibility terms for the Gamma lift and slice projection,
- a stationarity condition stated before comparison to zero data.

### Diagnostic Uses

Before it can support theorem-level claims, `C_3(q)` can guide the analytic
program by asking:

- whether a proposed `phi_q` class is stable under the required symmetries,
- whether the energy term has the expected sign behavior in test cases,
- whether lift and slice defects expose incompatible modeling choices,
- whether the candidate can be compared with zero data without using zero
  locations as inputs.

### Failure Modes

- The test-object assignment `q -> phi_q` may encode the desired answer.
- The energy term may be positive for reasons unrelated to RH-equivalent
  criteria.
- The lift and slice defect terms may dominate the Weil-type term and obscure
  the analytic target.
- A numerical comparison may look persuasive while still lacking a coercivity
  theorem.

### Theorem-Level Obligations

Before this candidate can carry proof weight, the program would need to define
the test-object class, state the sign or coercivity target, and prove that the
resulting energy is equivalent to, or rigorously implies, a known classical
positivity criterion. Any stationarity-to-zero bridge must be non-circular:
stationarity conditions must be specified before zero data is used for
diagnostics.

## Comparison Table

| Candidate | Ranking | Can currently test | Cannot yet claim | Proof-weight obligation |
| --- | --- | --- | --- | --- |
| `C_1(q; u)` | Safest | Slice projection, `Xi(s)` normalization, `s -> 1-s` residuals | Zero detection or off-slice control | Extract a nontrivial condition without circular use of classical symmetry |
| `C_2(q)` | Intermediate | Gamma-lift conjugacy and branch/domain consistency | A zeta-zero link or full completed-zeta symmetry | Construct `Gamma_H(q)` rigorously and connect it to the completed-zeta factors |
| `C_3(q)` | Boldest | Candidate positivity, coercivity, and explicit-formula compatibility | RH-equivalent consequence or stationarity-to-zero theorem | Prove a sign/coercivity bridge to a known classical criterion |

## Working Interpretation

Use the candidates in order:

- `C_1(q; u)` as the classical normalization baseline,
- `C_2(q)` as the quaternionic lift and conjugacy diagnostic,
- `C_3(q)` as the long-term analytic target.

The development path should keep diagnostic agreement separate from theorem
claims. A candidate becomes mathematically significant only when its domain,
regularity, symmetry, stationarity, and off-slice control are stated without
circular dependence on the desired zero locations.
