# Mirror Scaling And EigenRing Invariance

This document records why `Re(s)=1/2` is the unique mirror-balanced scale axis
and how quaternionic EigenRing geometry supports that picture without proving
zero locations.

## Prime Mirror Handshake

Let

```text
s = sigma + i t.
```

For a prime `p`,

```text
p^(-s) = p^(-sigma) exp(-i t log p).
```

The reflected point is

```text
1-s = 1-sigma - i t,
```

so

```text
p^(-(1-s)) = p^(-(1-sigma)) exp(+i t log p).
```

The reflected amplitudes match exactly when

```text
p^(-sigma) = p^(-(1-sigma)).
```

Since `p > 1`, this is equivalent to

```text
sigma = 1/2.
```

This is the prime mirror handshake: every local prime phase and its reflected
partner have equal amplitude only on `Re(s)=1/2`.

## Scaling Interpretation

The factor

```text
x^(-s) = x^(-sigma) exp(-i t log x)
```

shows that `t` is an oscillatory frequency in log-scale while `sigma` controls
scale weight. Moving away from `sigma=1/2` biases one reflected side over the
other.

The promising proof target is therefore not a raw geometric claim. It is a
scale-stability claim:

```text
mirror symmetry + completed analytic envelope + positivity/coercivity
  -> cancellation can be stable only at sigma=1/2.
```

This statement is not yet proved. It identifies the analytic object the repo is
trying to build. The next classical object is the scale-stability defect
`S_Xi(s)`, which must be defined before any quaternionic lift is used.

## Completed Mirror Envelope

The completed zeta function

```text
Xi(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) zeta(s)
```

satisfies

```text
Xi(s) = Xi(1-s).
```

The Gamma/factorial and `pi` factors are part of the mirror-balanced envelope.
They do not generate zeros by themselves, but they are essential to the clean
functional symmetry.

The Euler product is not normally convergent on `Re(s)=1/2`, so the local
prime-handshake identity cannot be promoted to a global zero-location argument
without a legitimate completed-zeta, explicit-formula, or regularized
coherence construction.

## EigenRing Invariance Lemma

Let `u` be a unit imaginary quaternion:

```text
u^2 = -1.
```

Let a critical-slice point be

```text
q = 1/2 + tau u.
```

For a unit quaternion `v`, define

```text
R_v(q) = v q v^(-1).
```

Because real scalars commute,

```text
R_v(q) = 1/2 + tau (v u v^(-1)).
```

The direction

```text
u' = v u v^(-1)
```

is again a unit imaginary quaternion. Therefore

```text
Re(R_v(q)) = 1/2,
||Im(R_v(q))|| = |tau|.
```

Unit quaternion rotations preserve the critical real coordinate and the shell
radius. If a shell is already placed as

```text
q_n(u) = 1/2 + t_n u,
```

then its rotated image is

```text
R_v(q_n(u)) = 1/2 + t_n (v u v^(-1)).
```

This is the EigenRing role: it preserves critical shells already supplied by
the analytic zeta condition or by a future non-circular theorem. It does not
derive the ordinates `t_n`.

## Forbidden Uses

- Do not claim the local prime handshake proves RH.
- Do not use the Euler product naively on `Re(s)=1/2`.
- Do not claim EigenRing rotation generates zeta zeros.
- Do not define a mirror stress by summing over primes unless an admissible
  regularization or explicit-formula interpretation is specified.
