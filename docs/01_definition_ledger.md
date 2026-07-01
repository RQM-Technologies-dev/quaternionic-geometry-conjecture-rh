# Definition Ledger

This ledger is the canonical source for notation and modeling defaults. It is a
v0 specification, not a completed analytic construction.

## Complex Variable And Reflection

Use

```text
s = sigma + i t.
```

The functional-equation reflection is

```text
R(s) = 1-s = 1-sigma - i t.
```

Complex conjugation is

```text
conj_C(sigma + i t) = sigma - i t.
```

Reflection and conjugation are different operations. Reflection changes the
real coordinate around `1/2`; conjugation changes the sign of the imaginary
coordinate.

For a prime `p`, the local phase factor is

```text
p^(-s) = p^(-sigma) exp(-i t log p).
```

Its reflected partner has amplitude `p^(-(1-sigma))`. These amplitudes match
if and only if `sigma=1/2`.

## Quaternionic Bookkeeping Domain

The ambient quaternion algebra is

```text
H = {a + b i + c j + d k : a,b,c,d in R}.
```

For

```text
q = a + b i + c j + d k,
```

define

```text
Re(q) = a,
Im(q) = b i + c j + d k.
```

Quaternionic conjugation is

```text
conj_H(q) = Re(q) - Im(q).
```

The Euclidean quaternion norm is

```text
||r + x i + y j + z k|| = sqrt(r^2 + x^2 + y^2 + z^2).
```

It matches the complex modulus on each complex slice.

## Slice Family And Projection

An admissible slice direction is a unit imaginary quaternion `u` satisfying

```text
u^2 = -1.
```

The corresponding slice is

```text
L_u = {a + t u : a,t in R}.
```

For `q = a + t u` in `L_u`, define

```text
pi_u(q) = a + i t = s.
```

The critical slice condition is

```text
Re(q) = 1/2.
```

On a fixed `L_u`, this projects to `Re(s)=1/2`.

## Completed-Zeta Normalization

Use

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s).
```

The classical input is

```text
Xi(s) = Xi(1-s).
```

This is established complex zeta theory. Any quaternionic construction must say
whether it is using a classical slice value, a lifted value, or a diagnostic
residual.

Define the Gamma/pi completion envelope

```text
A(s) = pi^(-s/2) Gamma(s/2).
```

Its reflected partner is

```text
A(1-s) = pi^(-(1-s)/2) Gamma((1-s)/2).
```

The completed zeta function can be read as the polynomial factor times
`A(s) zeta(s)`. The envelope `A(s)` is part of the completed mirror geometry;
it does not generate zeros by itself.

## Classical Scale-Stability Target

The immediate definition target is a real-valued scale-stability defect

```text
S_Xi(s).
```

Candidate v0 uses the completed mirror-angle defect. Write

```text
s = 1/2 + alpha + i t,
alpha = Re(s) - 1/2.
```

The same-height mirror point is

```text
s# = 1 - conj_C(s) = 1/2 - alpha + i t.
```

The candidate assumes a completed log-scale representation

```text
Xi(1/2 + z) = integral_R Phi_Xi(y) exp(z y) dy.
```

Normalize its completed scale measure by

```text
dmu_Xi(y) = Phi_Xi(y) dy / integral_R Phi_Xi(y) dy.
```

For theorem-level use, `Phi_Xi` and `mu_Xi` must be defined on a stated domain
with positivity, finiteness, non-degeneracy, and enough exponential moments.

Define

```text
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y).
```

Candidate v0 is

```text
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

Equivalently, it is the normalized `L^2(mu_Xi)` mirror-angle defect between
`f_s(y)=exp((s-1/2)y)` and `f_s#(y)=exp((s#-1/2)y)`.

This is a candidate definition, not a theorem. It is built from completed-zeta
data and the Gamma/pi-completed kernel, not from known zero locations.

The target theorem obligations are:

```text
S_Xi(s) = 0  =>  Re(s)=1/2,
Xi(s) = 0    =>  S_Xi(s)=0.
```

If both implications are proved for all nontrivial zeros in the intended
domain, they would imply the Riemann Hypothesis. At present Candidate v0 is a
definition target whose zero-to-stability bridge remains open.

The bridge-lemma naming is:

- Lemma A: completion transport supplies the positive, finite,
  non-degenerate completed scale measure `mu_Xi` from the Gamma/pi-completed
  kernel `Phi_Xi`;
- Lemma B: Candidate v0 has `S_Xi(s)=0 => Re(s)=1/2`;
- Lemma C: zeros satisfy `Xi(s)=0 => S_Xi(s)=0`.

Lemma C is the hard RH-level bridge. Lemma A may be interpreted
quaternionically through the Gamma/factorial completion layer only after the
classical completed kernel has been fixed.

## Quaternionic Completed Target

The completed quaternionic zeta target is

```text
Xi_H(q) = (1/2) q(q-1) pi^(-q/2) Gamma_H(q/2) Z_H(q).
```

Here:

- `Gamma_H(q/2)` is the Gamma/factorial completion layer.
- `Z_H(q)` is the still-undefined slice-compatible zeta side.
- `pi^(-q/2)` requires a branch and functional-calculus convention.
- multiplication order must be fixed before theorem-level use.

The candidate norm functional is

```text
C_QF_RH(q) = ||Xi_H(q)||^2.
```

This is the main research object, not a theorem.

## Gamma_H And Z_H Status

The guiding Gamma-lift expression is

```text
Gamma_H(q) = integral_0^infinity exp(-x) exp(q log x) dx.
```

Ledger status:

- on a fixed slice `L_u`, `Gamma_H(a + t u)` should agree with the compatible
  complex Gamma continuation after branch and domain choices are made;
- off-slice `Gamma_H(q)` remains conjectural until a quaternionic functional
  calculus is fixed;
- `Z_H(q)` remains undefined beyond the requirement that it restricts to the
  appropriate zeta-side expression on admissible slices.

## Non-Circularity Rules

Any future stationarity-to-zero claim must satisfy these rules.

- Do not define `S_Xi(s)`, `C_QF_RH(q)`, or any auxiliary stress using known
  zero locations.
- Do not tune slices, norms, branches, or test objects to force agreement with
  tabulated zeros.
- Specify domain, regularity, symmetry, norm, and stationarity before comparing
  to zero data.
- State the direction of implication before using it: zero to stationarity,
  stationarity to zero, or equivalence.
- Treat zero data as diagnostic guidance only.
- Do not make proof-weight claims until off-axis control has a stated sign,
  coercive, variational, or positivity structure.
