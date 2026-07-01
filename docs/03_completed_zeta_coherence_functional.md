# Completed Zeta Stability Conjecture

This document defines the Completed Zeta Stability Conjecture: first a
classical completed-zeta scale-stability defect `S_Xi(s)`, then a quaternionic
lift of that target.

The target is conjectural. It is not a proof of RH.

The conjectural shape is:

```text
Xi(s)=0  =>  S_Xi(s)=0  =>  Re(s)=1/2.
```

The first implication is the hard zero-to-stability bridge. The second is the
scale-stability axis claim supplied by Candidate v0 under the stated completed
kernel assumptions.

## Classical Input

The classical completed zeta function is

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s).
```

It satisfies

```text
Xi(s) = Xi(1-s).
```

This symmetry is the established analytic input. The repository studies how to
turn the mirror midpoint into a non-circular coherence or positivity condition.

## Gamma/pi Completion Envelope

Write

```text
A(s) = pi^(-s/2) Gamma(s/2).
```

The reflected envelope is

```text
A(1-s) = pi^(-(1-s)/2) Gamma((1-s)/2).
```

In this bookkeeping:

- `zeta(s)` is the prime/discrete/oscillatory side.
- `A(s)` is the continuum/curvature/completion side.
- `Xi(s)` is the mirror-balanced completed object where these pieces are
  normalized together, along with the polynomial factor `(1/2) s(s-1)`.

Gamma/pi completion does not generate zeta zeros, and it does not prove RH.
Its role is to put the zeta-side cancellation inside the completed mirror
geometry where `Xi(s)=Xi(1-s)` is a classical identity.

## Classical Core

The immediate target is a real-valued scale-stability defect

```text
S_Xi(s).
```

Candidate v0 below is the first precise proposed definition. It remains a
definition target, not a theorem. It is built from:

- the completed zeta function `Xi(s)`,
- the reflection `s -> 1-s`,
- the completion envelopes `A(s)` and `A(1-s)`,
- an admissible log-scale or test-function structure,
- a norm, energy, or stress interpretation stated before diagnostics.

`S_Xi(s)` must not use known zero locations, tabulated ordinates, or tuning
against numerical zero data.

A viable schematic target is:

```text
S_Xi(s) = completed_mirror_defect(Xi, A, A(1-s), admissible test data).
```

This means `S_Xi(s)` should measure failure of completed mirror stability, not
only mismatch of local prime amplitudes.

The clean RH-relevant target is the implication pair

```text
S_Xi(s) = 0  =>  Re(s)=1/2,
Xi(s) = 0    =>  S_Xi(s)=0.
```

The first implication is the off-axis coercivity target. The second is the
zero-to-stability bridge. If both are proved for the intended nontrivial-zero
domain, then zeros of `Xi` would have to lie on `Re(s)=1/2`.

This is the classical core. Quaternionic notation should not be used to bypass
these two obligations.

## Candidate Definition v0: Completed Mirror-Angle Defect

Write

```text
s = 1/2 + alpha + i t.
```

Define the same-height mirror point

```text
s# = 1 - conj_C(s) = 1/2 - alpha + i t.
```

This is different from the functional-equation reflection `1-s`; it reflects
the real coordinate across `1/2` while preserving the height `t`.

Candidate v0 assumes a completed log-scale kernel representation

```text
Xi(1/2 + z) = integral_R Phi_Xi(y) exp(z y) dy.
```

The kernel `Phi_Xi` is part of the Gamma/pi-completed object. For theorem use,
the representation must be fixed on a stated domain and must supply a positive,
finite, non-degenerate normalized scale measure

```text
dmu_Xi(y) = Phi_Xi(y) dy / integral_R Phi_Xi(y) dy.
```

The assumptions are:

- positivity: `dmu_Xi` is a positive measure on the chosen real log-scale;
- finiteness: the normalizing integral is finite and nonzero;
- non-degeneracy: `mu_Xi` is not concentrated at a single log-scale point;
- domain: the exponential moments below exist for the intended `alpha` range.

Define mirror scale profiles

```text
f_s(y)  = exp((s - 1/2) y),
f_s#(y) = exp((s# - 1/2) y).
```

With the `L^2(mu_Xi)` inner product, define

```text
S_Xi(s)
=
1
-
|<f_s, f_s#>_mu|^2
/
(||f_s||_mu^2 ||f_s#||_mu^2).
```

Equivalently, set

```text
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y).
```

Then Candidate v0 gives

```text
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

This form is non-circular: it uses the completed `Xi` kernel and its Gamma/pi
envelope, not known zero ordinates. Under the positivity, finiteness, and
non-degeneracy assumptions, Cauchy-Schwarz gives the conditional Lemma B proof
recorded in [05_candidate_v0_lemma_b_proof.md](05_candidate_v0_lemma_b_proof.md):

```text
S_Xi(s) >= 0,
S_Xi(s) = 0  =>  alpha = 0.
```

That is Lemma B, the off-axis instability statement. It does not prove RH by
itself. The hard theorem-level bridge remains Lemma C:

```text
Xi(s) = 0  =>  S_Xi(s)=0.
```

Only Lemma B plus Lemma C would force nontrivial zeros onto `Re(s)=1/2`,
after the completed kernel assumptions are supplied.

## Bridge Lemma Program

The Quaternionic Factorial/Gamma intuition should enter as a transport
principle for the completed envelope, not as a zero generator. The proof route
is organized as three lemmas.

Lemma A: completion transport.

```text
Gamma/pi completion, and its slice-compatible Gamma/factorial interpretation,
supplies the completed scale kernel Phi_Xi and normalized measure mu_Xi.
```

For Candidate v0, [06_lemma_a_theta_kernel_construction.md](06_lemma_a_theta_kernel_construction.md)
constructs this measure from the classical theta kernel and records positivity,
finiteness, non-degeneracy, and exponential moments. Quaternionic or factorial
language may interpret the completion geometry after this classical kernel is
fixed, but it must not define the kernel from zero data.

Lemma B: mirror-axis uniqueness.

```text
S_Xi(s)=0  =>  Re(s)=1/2.
```

For Candidate v0, this is the Cauchy-Schwarz equality-case statement proved
conditionally in [05_candidate_v0_lemma_b_proof.md](05_candidate_v0_lemma_b_proof.md)
once Lemma A supplies the measure assumptions.

Lemma C: zero-to-stability bridge.

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

This is the RH-hard step. It must show that completed zeta cancellation forces
the completed mirror-angle stability measured by `S_Xi`, without using known
zero ordinates or tuning the measure to the zero list. The current bridge audit
is [07_weil_explicit_formula_bridge.md](07_weil_explicit_formula_bridge.md),
which redirects Lemma C toward explicit-formula positivity.

The intended conclusion is:

```text
Lemma A + Lemma B + Lemma C
  => all nontrivial zeros in the intended domain satisfy Re(s)=1/2.
```

## Hyper-Spherical Interpretation

The supporting hyperspherical picture uses the critical-slice form

```text
q = 1/2 + tau u,
```

where `u^2=-1`. This geometry visualizes completed mirror-stable shells after
the classical object has been defined. It can help organize the shell language
for a later quaternionic lift, but it does not generate zeta zeros and it does
not replace the classical proof burden.

The proof burden remains:

```text
define S_Xi(s),
prove completion transport for mu_Xi,
prove S_Xi(s)=0 => Re(s)=1/2,
prove Xi(s)=0 => S_Xi(s)=0.
```

## Quaternionic Lift Target

After `S_Xi(s)` is specified, the quaternionic completed target is

```text
Xi_H(q) = (1/2) q(q-1) pi^(-q/2) Gamma_H(q/2) Z_H(q).
```

The associated norm functional is

```text
C_QF_RH(q) = ||Xi_H(q)||^2.
```

Interpretation:

- `Gamma_H(q/2)` supplies the Gamma/factorial completion envelope.
- `Z_H(q)` supplies the zeta-side cancellation structure once defined.
- `C_QF_RH(q)` is the candidate shell/coherence surface lifting the classical
  `S_Xi` target.
- On a fixed admissible slice, `Xi_H(q)` should reduce to the classical
  completed-zeta expression after projection.

Off-slice, `Xi_H(q)` remains a research target until `Gamma_H`, `Z_H`, branch
choices, multiplication order, and functional calculus are fixed.

## Desired Coherence Property

The desired theorem-level shape is:

```text
classical scale-stability defect S_Xi
  + completion transport
  + off-axis coercivity
  + zero-to-stability bridge
  -> zeros of Xi lie on Re(s)=1/2.
```

The quaternionic extension can then be read as:

```text
completed mirror symmetry
  + prime/phase cancellation
  + non-circular positivity, coercivity, or stationarity condition
  -> scale-stable cancellation only at Re(s)=1/2.
```

The hard part is excluding off-line mirrored pairs. The functional equation
alone only says that zeros occur in reflected pairs. It does not rule out
off-line pairs.

## Reduced Supporting Candidates

The older candidate functionals are retained only as support tests.

| Candidate | Current role | Cannot claim |
| --- | --- | --- |
| Classical `S_Xi(s)` defect | Immediate definition target for scale-stability | Any RH consequence until both implications are proved |
| Slice completed-zeta residual | Checks `Xi(s)`, projection, and reflection conventions | Zero detection, because exact `Xi(s)=Xi(1-s)` already vanishes as a residual |
| Gamma-lift conjugacy defect | Tests branch/domain behavior of `Gamma_H` | A zeta-zero link without `Z_H` and completed structure |
| Weil/explicit-formula energy | Best long-term route toward positivity/coercivity | RH consequence until connected to a known criterion non-circularly |

The main classical object is `S_Xi(s)`. The quaternionic object
`C_QF_RH(q)` should lift that core rather than multiply independent proof
routes.

## Zero Shells And Completion Weights

If `t_n` is a positive ordinate of a nontrivial zero, the diagnostic shell is

```text
q_n(u) = 1/2 + t_n u.
```

The completed object evaluates the Gamma/factorial envelope on that shell. This
does not mean Gamma generates the zero. It means the zero shell is studied
inside the completed mirror geometry.

Known `t_n` values may be used only after `S_Xi(s)` or its quaternionic lift is
defined, and only to test whether diagnostics reproduce expected shell
behavior.

## Proof-Weight Requirements

Before `S_Xi(s)` can carry theorem weight beyond the conditional Lemma A and
Lemma B route, the program must specify:

- its domain in the critical strip or completed-zeta domain;
- the completed kernel `Phi_Xi` and normalized measure `mu_Xi`;
- positivity, finiteness, non-degeneracy, and moment assumptions;
- Lemma A, the completion-transport proof for `mu_Xi`, as recorded for
  Candidate v0 in
  [06_lemma_a_theta_kernel_construction.md](06_lemma_a_theta_kernel_construction.md);
- Lemma B, the off-axis coercivity proof for Candidate v0, as recorded in
  [05_candidate_v0_lemma_b_proof.md](05_candidate_v0_lemma_b_proof.md);
- Lemma C, the zero-to-stability statement `Xi(s)=0 => S_Xi(s)=0`, with the
  explicit-formula bridge audited in
  [07_weil_explicit_formula_bridge.md](07_weil_explicit_formula_bridge.md).

Before `C_QF_RH(q)` can carry theorem weight as a lift, the program must also
specify:

- the domain of `q`;
- the admissible slice family;
- `Gamma_H(q)` and `Z_H(q)`;
- branch and multiplication-order conventions;
- the norm or energy structure;
- the stationarity, positivity, or coercivity condition;
- the implication direction connecting the condition to zeros.

Without these, `S_Xi(s)` is a definition target and `C_QF_RH(q)` is a
quaternionic research target.
