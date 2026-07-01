# Candidate v0 Core

This document is the compact core of the current proof route. It records the
Completed Zeta Stability Conjecture, the Candidate v0 definition, Lemma A, and
Lemma B. Lemma C remains open and is handled in
[03_lemma_c_weil_bridge.md](03_lemma_c_weil_bridge.md).

## Conjecture Target

The target is a non-circular completed-zeta stability defect `S_Xi(s)` such
that

```text
Xi(s)=0  =>  S_Xi(s)=0  =>  Re(s)=1/2.
```

The right implication is the mirror-axis uniqueness side. The left implication
is the zero-to-stability bridge.

The local mirror-scaling algebra is:

```text
p^(-sigma) = p^(-(1-sigma))  iff  sigma=1/2.
```

This marks the critical line as the unique local amplitude-balance axis. It is
not used as an Euler-product argument in the critical strip.

## Lemma A: Completed Scale Measure

Use

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s),
s = 1/2 + z.
```

The classical theta-kernel representation gives

```text
Xi(1/2 + z) = integral_R Phi_Xi(y) exp(z y) dy.
```

For `y >= 0`, take

```text
Phi_+(y)
=
2 pi exp(5y/2)
sum_{n>=1}
  (2 pi n^2 exp(2y) - 3) n^2 exp(-pi n^2 exp(2y)).
```

Define the even kernel

```text
Phi_Xi(y) = Phi_+(|y|).
```

For `y >= 0` and `n >= 1`,

```text
2 pi n^2 exp(2y) - 3 >= 2 pi - 3 > 0,
```

so `Phi_Xi(y)>0`. The factor `exp(-pi n^2 exp(2|y|))` gives
super-exponential decay, hence

```text
integral_R exp(beta y) Phi_Xi(y) dy < infinity
```

for every real `beta`.

Normalize

```text
Z_Xi = integral_R Phi_Xi(y) dy = Xi(1/2),
dmu_Xi(y) = Phi_Xi(y) dy / Z_Xi.
```

Then `mu_Xi` is positive, normalized, finite, non-degenerate, independent of
known zero ordinates, and has all real exponential moments. This is Candidate
v0's Lemma A input:

```text
Gamma/pi completed theta kernel -> Phi_Xi -> mu_Xi.
```

## Candidate v0 Definition

Write

```text
s = 1/2 + alpha + i t.
```

Define

```text
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y).
```

The Candidate v0 scale-stability defect is

```text
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

The height `t` cancels from this mirror-angle ratio. Candidate v0 therefore
detects the real scale axis; it does not by itself control zero ordinates.

## Lemma B: Mirror-Axis Uniqueness

Because `mu_Xi` is normalized,

```text
integral_R 1 dmu_Xi(y) = 1.
```

For real `alpha`, set

```text
g_alpha(y) = exp(alpha y),
g_-alpha(y) = exp(-alpha y).
```

Then `g_alpha(y) g_-alpha(y)=1`, and Cauchy-Schwarz gives

```text
1
= |<g_alpha, g_-alpha>_mu|^2
<= ||g_alpha||_mu^2 ||g_-alpha||_mu^2
= M(alpha) M(-alpha).
```

Therefore

```text
S_Xi(s) >= 0.
```

Equality in Cauchy-Schwarz requires `exp(2 alpha y)` to be constant
`mu_Xi`-almost everywhere. Since `mu_Xi` is non-degenerate, this can happen
only when `alpha=0`. Conversely, if `alpha=0`, then `M(0)=1` and `S_Xi(s)=0`.
Thus

```text
S_Xi(s)=0  iff  alpha=0  iff  Re(s)=1/2.
```

This proves Lemma B for Candidate v0 under the Lemma A measure assumptions.

## Remaining Bridge

Lemma A and Lemma B do not imply that a zero of `Xi` satisfies `S_Xi(s)=0`.
The remaining theorem-level obligation is Lemma C:

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

For Candidate v0, Lemma C must explain why completed zeta cancellation forces
equality in the Cauchy-Schwarz inequality above. Functional-equation symmetry
alone is not enough, because it permits reflected off-line pairs unless an
additional positivity, coercivity, variational, or explicit-formula mechanism
rules them out.

## Quaternionic Status

Quaternionic and EigenRing language may interpret completed mirror-stable
shells after the classical object has been defined. It must not define
`Phi_Xi`, `mu_Xi`, or `S_Xi` from zero data, and it must not replace Lemma C.
