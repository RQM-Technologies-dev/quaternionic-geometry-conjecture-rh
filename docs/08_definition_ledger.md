# Definition Ledger

This ledger records the current modeling defaults for the conjecture program.
It is a v0 specification, not a final analytic construction. Later diagnostic
or theorem-development work should cite this file when it relies on a domain,
projection, conjugation, normalization, or functional choice.

## Ambient Quaternionic Domain

The ambient space is the quaternion algebra

```text
H = {a + b i + c j + d k : a,b,c,d in R}.
```

For a quaternion

```text
q = a + b i + c j + d k,
```

the real part is

```text
Re(q) = a,
```

and the imaginary part is

```text
Im(q) = b i + c j + d k.
```

The current analytic status is conservative:

- `H` is the ambient bookkeeping domain.
- Any analytic claim about `Gamma_H(q)` or `C(q)` must later specify its actual
  domain, excluded points, branch choices, and regularity class.
- Off-slice quaternionic behavior is a conjectural development target until a
  precise functional calculus is fixed.

## Admissible Slice Family

An admissible slice direction is a unit imaginary quaternion `u` satisfying

```text
u^2 = -1.
```

The corresponding complex slice is

```text
L_u = {a + t u : a,t in R}.
```

Each `L_u` is treated as a complex plane inside `H`. The critical slice is the
real-affine condition

```text
Re(q) = 1/2.
```

On a fixed `L_u`, this becomes the projected critical line.

## Projection Map

For `q = a + t u` in `L_u`, define the slice projection

```text
pi_u(q) = a + i t = s.
```

The projection is slice-dependent. A real quaternion `q = a` lies in every
slice, so `pi_u(a) = a` for every admissible `u`. When a construction records
which slice produced a real-axis point, the selected `u` is bookkeeping data,
not a different complex value.

## Conjugations And Reflection

The program distinguishes three operations.

| Operation | Formula | Status |
| --- | --- | --- |
| Quaternionic conjugation | `conj_H(q) = Re(q) - Im(q)` | Definitional on `H`. |
| Complex conjugation | `conj_C(sigma + i t) = sigma - i t` | Classical on each projected slice. |
| Functional reflection | `R(s) = 1-s` | Classical zeta functional-equation reflection. |

On a fixed slice, if `q = a + t u` and `s = pi_u(q)`, then

```text
pi_u(conj_H(q)) = conj_C(s).
```

This is not the same operation as `s -> 1-s`. The reflection `s -> 1-s`
changes the real coordinate around `1/2`; conjugation changes the sign of the
imaginary coordinate.

## Completed-Zeta Normalization

Use the completed-zeta normalization

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s).
```

The classical input is the functional symmetry

```text
Xi(s) = Xi(1-s).
```

In this repository, this identity is treated as established classical zeta
theory. Any quaternionic construction that uses `Xi(s)` must say whether it is
using the classical projected value, a lifted value, or a diagnostic residual.

## Gamma-Lift Status

The guiding Gamma-lift target is

```text
Gamma_H(q) = integral_0^infinity exp(-x) exp(q log x) dx.
```

The ledger default is:

- on a fixed admissible slice `L_u`, `Gamma_H(a + t u)` is required to agree
  with the corresponding complex Gamma continuation after compatible domain and
  branch choices are made;
- away from fixed slice reductions, `Gamma_H(q)` remains conjectural until the
  program specifies a quaternionic functional calculus, branch convention, and
  multiplication-order convention;
- any off-slice use of `Gamma_H(q)` is therefore an analytic development
  target, not a theorem-level input.

## Norm Default For `C_2(q)`

For the Gamma-lift conjugacy defect, use the Euclidean quaternion norm

```text
||r + x i + y j + z k|| = sqrt(r^2 + x^2 + y^2 + z^2).
```

This norm matches the usual complex modulus on each slice. The current
candidate defect is therefore read as

```text
C_2(q) = ||Gamma_H(conj_H(q)) - conj_H(Gamma_H(q))||^2.
```

This is a diagnostic form until `Gamma_H(q)` is rigorously constructed on the
chosen domain.

## Candidate Functional Status

| Candidate | Classical components | Definitional components | Diagnostic components | Conjectural components |
| --- | --- | --- | --- | --- |
| `C_1(q; u)` | `Xi(s)`, `Xi(s)=Xi(1-s)` | `L_u`, `pi_u(q)`, reflection convention | completed-zeta residual as a normalization check | any nontrivial stationarity or zero-detection claim |
| `C_2(q)` | complex Gamma behavior on fixed slices | `conj_H`, Euclidean quaternion norm | Gamma-lift conjugacy residual | off-slice `Gamma_H(q)` and any link to zeta zeros |
| `C_3(q)` | explicit-formula and Weil-type positivity background | chosen test-object bookkeeping once defined | comparison of energy, lift defect, and slice defect | coercivity, sign-definiteness, and stationarity-to-zero bridge |

The status labels mean:

- Classical: imported from established complex zeta or Gamma theory.
- Definitional: a repository modeling choice recorded by this ledger.
- Diagnostic: useful for comparison, normalization, or target selection.
- Conjectural: not available as proof-weight input without later analytic work.

## Non-Circularity Rules

Any future stationarity-to-zero claim must satisfy these rules.

- Do not define `C(q)` using known zero locations.
- Do not tune admissible slices, norms, branches, or test objects to force
  agreement with tabulated zeros.
- Specify the domain, regularity, symmetry, and stationarity conditions before
  comparing outputs to zero data.
- Treat zero data as diagnostic guidance only.
- State which implication is being claimed before using it: stationarity to
  zero, zero to stationarity, or an equivalence.
- Do not make proof-weight claims until off-slice control has a stated sign,
  coercive, or variational structure.

The ledger standard is deliberately narrow: definitions first, diagnostics
second, theorem-level claims only after the analytic obligations are explicit.
