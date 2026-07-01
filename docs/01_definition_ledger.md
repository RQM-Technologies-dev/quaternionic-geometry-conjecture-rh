# Definition Ledger

This ledger is the canonical notation and assumption record for the Completed
Zeta Stability Conjecture. It is a v0 specification, not a completed analytic
construction.

## Complex Variable And Reflection

Use

```text
s = sigma + i t = 1/2 + alpha + i t,
alpha = Re(s) - 1/2.
```

The functional-equation reflection and complex conjugation are different:

```text
R(s) = 1 - s = 1 - sigma - i t,
conj_C(sigma + i t) = sigma - i t.
```

The same-height mirror point used by Candidate v0 is

```text
s# = 1 - conj_C(s) = 1/2 - alpha + i t.
```

For a prime `p`,

```text
p^(-s) = p^(-sigma) exp(-i t log p),
```

and the reflected local amplitude is `p^(-(1-sigma))`. These amplitudes match
if and only if `sigma=1/2`.

## Completed Zeta Normalization

Use the completed zeta function

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s).
```

The established classical symmetry is

```text
Xi(s) = Xi(1-s).
```

The Gamma/pi envelope is

```text
A(s) = pi^(-s/2) Gamma(s/2).
```

This envelope is part of the completed mirror geometry. It does not generate
zeros by itself.

## Candidate v0 Objects

Candidate v0 assumes the completed log-scale representation

```text
Xi(1/2 + z) = integral_R Phi_Xi(y) exp(z y) dy,
```

where `Phi_Xi` is the positive even theta kernel fixed in
[02_candidate_v0_core.md](02_candidate_v0_core.md). Normalize

```text
dmu_Xi(y) = Phi_Xi(y) dy / integral_R Phi_Xi(y) dy.
```

For theorem-level use, `mu_Xi` must be positive, finite, non-degenerate,
independent of known zero ordinates, and equipped with the required exponential
moments.

Define

```text
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y).
```

Candidate v0 is the completed mirror-angle defect

```text
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

Equivalently, it is the normalized `L^2(mu_Xi)` mirror-angle defect between
`exp((s-1/2)y)` and `exp((s#-1/2)y)`.

## Bridge Lemma Program

The proof route is organized as:

```text
Lemma A:
  Gamma/pi completed theta kernel -> Phi_Xi -> mu_Xi.

Lemma B:
  S_Xi(s)=0 => Re(s)=1/2.

Lemma C:
  Xi(s)=0 => S_Xi(s)=0.
```

For Candidate v0, Lemma A and Lemma B are recorded in
[02_candidate_v0_core.md](02_candidate_v0_core.md). Lemma C is the active
RH-level bridge and is tracked in
[03_lemma_c_weil_bridge.md](03_lemma_c_weil_bridge.md).

If Lemma C and Lemma B are proved for all nontrivial zeros in the intended
domain, the zeros lie on `Re(s)=1/2`. Until then, Candidate v0 remains a
conjectural proof route.

## Quaternionic Bookkeeping

The ambient quaternion algebra is

```text
H = {a + b i + c j + d k : a,b,c,d in R}.
```

For `q = a + b i + c j + d k`, define

```text
Re(q)=a,
Im(q)=b i + c j + d k,
conj_H(q)=Re(q)-Im(q).
```

An admissible slice direction is a unit imaginary quaternion `u` with `u^2=-1`,
and the slice is

```text
L_u = {a + t u : a,t in R}.
```

On `L_u`, the projection is

```text
pi_u(a + t u) = a + i t.
```

The critical slice condition is

```text
Re(q)=1/2,
```

which projects to `Re(s)=1/2`. When a fixed quaternionic shell is also chosen,
this may be read as the critical-sphere slice. This geometry is interpretive
unless Lemma C supplies the analytic zero-to-stability bridge.

The later quaternionic target is

```text
Xi_H(q) = (1/2) q(q-1) pi^(-q/2) Gamma_H(q/2) Z_H(q),
C_QF_RH(q) = ||Xi_H(q)||^2.
```

`Gamma_H`, `Z_H`, branch choices, multiplication order, and functional calculus
remain analytic development targets.

## Non-Circularity Rules

- Do not define `S_Xi(s)`, `C_QF_RH(q)`, or auxiliary stress terms using known
  zero locations.
- Do not tune slices, norms, branches, measures, or test functions to tabulated
  zeros.
- Specify domain, regularity, symmetry, norm, and implication direction before
  comparing to zero data.
- Treat zero data as diagnostics only after the analytic object is fixed.
- Keep quaternionic geometry downstream of the classical completed-zeta object.
- Do not make proof-weight claims until off-axis control has a sign,
  coercive, variational, or positivity structure.
