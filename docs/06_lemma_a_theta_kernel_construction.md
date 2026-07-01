# Lemma A Theta-Kernel Construction

This note records the Candidate v0 construction for Lemma A. It uses the
classical Riemann theta-kernel representation of the completed zeta function to
produce the positive completed scale measure `mu_Xi` required by the Lemma B
proof.

This is not a proof of the Riemann Hypothesis. It supplies the measure side of
Candidate v0. The RH-level bridge

```text
Xi(s)=0  =>  S_Xi(s)=0
```

remains open.

## Classical Theta-Kernel Input

Let

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s).
```

Write

```text
s = 1/2 + z.
```

The classical theta-kernel representation gives

```text
Xi(1/2 + z) = integral_R Phi_Xi(y) exp(z y) dy,
```

where `Phi_Xi` is the even extension of the positive Riemann theta kernel. For
`y >= 0`, use the explicit kernel

```text
Phi_+(y)
=
sum_{n>=1}
  (4 pi^2 n^4 exp(9y/2) - 6 pi n^2 exp(5y/2))
  exp(-pi n^2 exp(2y)).
```

Equivalently,

```text
Phi_+(y)
=
2 pi exp(5y/2)
sum_{n>=1}
  (2 pi n^2 exp(2y) - 3) n^2 exp(-pi n^2 exp(2y)).
```

Define

```text
Phi_Xi(y) = Phi_+(|y|).
```

Then

```text
Xi(1/2 + z)
=
integral_R Phi_Xi(y) exp(z y) dy.
```

This is the completed log-scale representation required by Candidate v0. It is
classical input from the completed theta formulation, not a construction from
zero data.

## Positivity

For `y >= 0` and `n >= 1`,

```text
2 pi n^2 exp(2y) - 3 >= 2 pi - 3 > 0.
```

Every other factor in each summand is positive. Therefore

```text
Phi_+(y) > 0
```

for `y >= 0`, and the even extension gives

```text
Phi_Xi(y) > 0
```

for every real `y`.

## Finiteness And Moments

The factor

```text
exp(-pi n^2 exp(2|y|))
```

gives super-exponential decay as `|y| -> infinity`. Therefore

```text
integral_R Phi_Xi(y) dy < infinity,
```

and, for every real `beta`,

```text
integral_R exp(beta y) Phi_Xi(y) dy < infinity.
```

Thus the exponential moments needed by Candidate v0 exist for every real
`alpha` appearing in

```text
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y).
```

## Non-Degeneracy

Because `Phi_Xi(y) > 0` on every real interval, the measure below is not
concentrated at a single log-scale point. This supplies the non-degeneracy
assumption required by the Lemma B equality case.

## Normalized Completed Scale Measure

Set

```text
Z_Xi = integral_R Phi_Xi(y) dy = Xi(1/2).
```

Since `Phi_Xi` is positive and finite,

```text
0 < Z_Xi < infinity.
```

Define

```text
dmu_Xi(y) = Phi_Xi(y) dy / Z_Xi.
```

Then `mu_Xi` is:

- positive;
- normalized;
- finite;
- non-degenerate;
- independent of known zero ordinates;
- equipped with all real exponential moments.

This proves Lemma A for Candidate v0:

```text
Gamma/pi completed theta kernel -> Phi_Xi -> mu_Xi.
```

## Consequence For Candidate v0

With this `mu_Xi`, Candidate v0 has the moment function

```text
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y),
```

and the scale-stability defect

```text
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

The Lemma B note proves from these measure properties that

```text
S_Xi(s)=0  iff  Re(s)=1/2.
```

Thus Candidate v0 now has a completed measure construction and a conditional
mirror-axis uniqueness proof.

## Remaining Open Bridge

The remaining theorem-level target is Lemma C:

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

For this Candidate v0, Lemma C is equivalent to showing that every completed
zeta zero forces equality in the Cauchy-Schwarz inequality used by Lemma B.
That is the RH-level content. The theta-kernel construction does not by itself
exclude off-line reflected zero pairs.

Any next proof outline must therefore explain, without using zero ordinates, why
completed zeta cancellation forces Candidate v0 scale-stability.
