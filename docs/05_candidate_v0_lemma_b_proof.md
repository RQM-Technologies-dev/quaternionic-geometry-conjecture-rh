# Candidate v0 Lemma B Proof

This note records the conditional Lemma B proof for Candidate v0. It is a proof
of the mirror-axis uniqueness statement under the stated measure assumptions. It
is not a proof of the Riemann Hypothesis, because the zero-to-stability bridge

```text
Xi(s)=0  =>  S_Xi(s)=0
```

remains open.

## Status

Inputs and definitions:

- the completed zeta function `Xi(s)` satisfies `Xi(s)=Xi(1-s)`;
- Candidate v0 assumes a completed log-scale representation for `Xi`;
- the normalized completed scale measure `mu_Xi` is intended to be supplied by
  Lemma A.

Definitions:

- write `s = 1/2 + alpha + i t`;
- write the same-height mirror point as `s# = 1/2 - alpha + i t`;
- define

```text
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y);
```

- define Candidate v0 by

```text
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

The height `t` cancels from this mirror-angle ratio. Lemma B controls the real
scale coordinate `alpha`; it does not locate zero ordinates.

Conditional theorem:

```text
S_Xi(s) >= 0,
S_Xi(s)=0  =>  Re(s)=1/2.
```

This is Lemma B. Its measure assumptions are supplied for Candidate v0 by
[06_lemma_a_theta_kernel_construction.md](06_lemma_a_theta_kernel_construction.md).

## Assumptions

Let `mu_Xi` be a positive normalized measure on the real log-scale variable
`y`. For the chosen real `alpha`, assume:

1. `M(alpha)` and `M(-alpha)` are finite.
2. `mu_Xi` is non-degenerate: it is not concentrated at a single value of `y`.
3. `mu_Xi` is obtained independently of zero ordinates.

The third condition is a non-circularity condition. It is not needed for the
Cauchy-Schwarz inequality itself, but it is required before the argument can
carry proof weight in this program.

## Proof

Because `mu_Xi` is normalized,

```text
integral_R 1 dmu_Xi(y) = 1.
```

For real `alpha`, write

```text
g_alpha(y) = exp(alpha y),
g_-alpha(y) = exp(-alpha y).
```

Then

```text
g_alpha(y) g_-alpha(y) = 1.
```

Apply Cauchy-Schwarz in `L^2(mu_Xi)`:

```text
1
= |<g_alpha, g_-alpha>_mu|^2
<= ||g_alpha||_mu^2 ||g_-alpha||_mu^2
= M(alpha) M(-alpha).
```

Therefore

```text
M(alpha) M(-alpha) >= 1
```

and Candidate v0 gives

```text
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)) >= 0.
```

Now consider equality. Equality in Cauchy-Schwarz holds exactly when
`g_alpha` and `g_-alpha` are linearly dependent `mu_Xi`-almost everywhere.
Thus there is a constant `c` such that

```text
exp(alpha y) = c exp(-alpha y)
```

for `mu_Xi`-almost every `y`, or equivalently

```text
exp(2 alpha y) = c.
```

If `alpha != 0`, this forces `y` to be constant `mu_Xi`-almost everywhere,
contradicting non-degeneracy. Therefore equality can occur only when
`alpha = 0`.

When `alpha = 0`,

```text
M(0) = integral_R 1 dmu_Xi(y) = 1,
S_Xi(s) = 1 - 1 = 0.
```

Hence, under the assumptions,

```text
S_Xi(s)=0  iff  alpha=0  iff  Re(s)=1/2.
```

This proves Lemma B for Candidate v0.

## What This Does Not Prove

The proof above does not prove that any zero of `Xi` satisfies
`S_Xi(s)=0`. It proves only that, if a point is scale-stable for Candidate v0,
then it lies on the critical line.

The remaining RH-level bridge is Lemma C:

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

For Candidate v0, Lemma C must explain why completed zeta cancellation at a
zero forces equality in the completed mirror-angle inequality. Symmetry
`Xi(s)=Xi(1-s)` alone is not enough, because the functional equation permits
off-line reflected pairs unless an additional positivity, coercivity, or
explicit-formula mechanism rules them out.

## Next Theorem Target

The next proof work should not re-prove Lemma B. With the Candidate v0 Lemma A
construction recorded separately, the next theorem target is Lemma C:

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

The required work is to identify a non-circular reason why `Xi(s)=0` forces
equality in the Candidate v0 Cauchy-Schwarz inequality. Until that is proved,
Candidate v0 remains a conjectural proof route inside the Completed Zeta
Stability Conjecture.
