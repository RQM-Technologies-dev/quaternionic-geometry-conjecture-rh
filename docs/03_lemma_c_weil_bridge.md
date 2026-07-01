# Lemma C Weil Bridge

This document is the active proof-gap note. It consolidates the Weil
explicit-formula route for Lemma C:

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

With Candidate v0 and Lemma B from
[02_candidate_v0_core.md](02_candidate_v0_core.md), Lemma C is the step that
would force a completed-zeta zero onto the mirror-stable axis.

## Bombieri-Weil Convention

Let `W` be Bombieri's test-function class on the positive half-line, with
Mellin transform

```text
tilde_f(s) = integral_0^infinity f(x) x^s dx / x.
```

For `f in W`, the explicit formula is written here as

```text
tilde_f(0) - sum_rho tilde_f(rho) + tilde_f(1)
=
sum_{n>=1} Lambda(n) { f(n) + (1/n) f(1/n) }
+ (log(4*pi) + gamma) f(1)
+ integral_1^infinity
    { f(x) + (1/x) f(1/x) - (2/x) f(1) }
    dx / (x - x^(-1)).
```

Call the right-hand side `W_B(f)`. The zero sum is understood by symmetric
height truncation. Bombieri's Weil criterion uses autocorrelations

```text
f(x) = integral_0^infinity g(x y) g(y) dy
```

with the two normalization constraints

```text
integral_0^infinity g(x) dx / x = 0,
integral_0^infinity g(x) dx = 0.
```

In this sign convention, the positivity route asks for

```text
W_B(f) <= 0
```

for every admissible autocorrelation.

## Candidate v0 Attachment

Assume an off-line zero

```text
rho0 = 1/2 + alpha + i tau,
alpha != 0.
```

The Candidate v0 bridge attempt constructs a height-aware admissible family
`f_{alpha,tau}` with

```text
tilde_f_{alpha,tau}(s)
= G_{alpha,tau}(s) G_{alpha,tau}(1-s),
G_{alpha,tau}(0)=G_{alpha,tau}(1)=0.
```

The endpoint terms vanish, so the explicit formula reduces to the zero side:

```text
W_B(f_{alpha,tau})
= - sum_rho G_{alpha,tau}(rho) G_{alpha,tau}(1-rho).
```

To close Lemma C by contradiction, an assumed off-line zero must force

```text
W_B(f_{alpha,tau}) > 0,
```

contradicting the Weil sign target. Equivalently, the zero side must satisfy

```text
sum_rho G_{alpha,tau}(rho) G_{alpha,tau}(1-rho) < 0.
```

The current obstruction is that Candidate v0 supplies an axis detector, not yet
a signed dominance theorem for the full zero sum.

## Zero-Orbit Dominance Target

Split the zero side into the selected orbit and the remaining zeros:

```text
sum_rho G(rho) G(1-rho)
= Z_orbit(alpha,tau) + Z_rest(alpha,tau).
```

A viable Lemma C bridge must prove:

```text
1. selected-orbit lower bound:
   |Z_orbit(alpha,tau)| >= c(alpha,tau) > 0;

2. tail bound:
   |Z_rest(alpha,tau)| < |Z_orbit(alpha,tau)|;

3. sign:
   Z_orbit(alpha,tau) + Z_rest(alpha,tau) < 0.
```

Without these estimates, an off-line zero may contribute a nonzero term but the
rest of the zero sum can cancel or dominate it.

It is useful to name the strengthened energy

```text
E_Weil(alpha,tau) = -W_B(f_{alpha,tau}).
```

The old two-dimensional expansion/shrinkage intuition becomes valid only if it
is expressed as a theorem about this explicit-formula energy:

```text
Xi(rho0)=0 and alpha != 0
  => E_Weil(alpha,tau) < 0.
```

## Gaussian-Window Direction

The current active construction is a parameterized localized family. Let

```text
Psi_T(u) = (1 / (sqrt(2*pi) T)) exp(-u^2 / (2 T^2)),
T > 0,
```

and set

```text
B_T(u) = N_T (E * Psi_T)(u).
```

If

```text
F_T(z) = integral_R B_T(u) exp(z u) du,
```

then formally

```text
F_T(z) = N_T K(z) exp(T^2 z^2 / 2).
```

On vertical offsets this supplies Gaussian suppression:

```text
|exp(T^2 (x+i eta)^2 / 2)|
= exp(T^2 (x^2 - eta^2) / 2).
```

Use a symmetric height-targeted seed

```text
h0_{alpha,tau,T}(u) = B_T(u) cos(tau u) sinh(alpha u),
```

then subtract two centering directions so that

```text
G_{alpha,tau,T}(0)=0,
G_{alpha,tau,T}(1)=0.
```

The corresponding autocorrelation has

```text
tilde_f_{alpha,tau,T}(s)
= G_{alpha,tau,T}(s) G_{alpha,tau,T}(1-s),
```

and the target estimates become

```text
|Z_orbit(alpha,tau,T)| >= c(alpha,tau) > 0,
|Z_rest(alpha,tau,T)| <= epsilon(T) c(alpha,tau),
epsilon(T) -> 0,
Z_orbit(alpha,tau,T) + Z_rest(alpha,tau,T) < 0.
```

## EigenCircle Interpretation

The legacy EigenCircle geometry is useful only as a diagnostic language for
selected-orbit survival. Its coordinate form is

```text
q = 1/2 + x i + y j + z k,
critical slice: Re(q)=1/2,
EigenCircle on a fixed shell: x^2 + y^2 = R0^2, z=0, Re(q)=1/2.
```

In current notation,

```text
alpha = 0  <=>  critical-slice / fixed-shell intersection,
alpha != 0 <=>  trajectory misses that critical slice.
```

Thus the geometric bridge obligation is only a restatement of Lemma C unless it
is derived from the Weil machinery:

```text
Xi(s)=0
  => selected orbit intersects the critical slice
  => S_Xi(s)=0.
```

## Active Proof Task

The next work item is not another note. It is the coefficient and tail estimate
inside this bridge:

- bound the centering coefficients `a_{alpha,tau,T}` and
  `b_{alpha,tau,T}`;
- prove vertical strip bounds for `K(z)`, `K'(z)`, and the Gaussian-convolved
  transforms;
- prove selected-orbit non-cancellation after centering;
- prove a zero-counting or zero-density tail bound strong enough to control
  `Z_rest`;
- decide whether the EigenCircle survival language adds structure or only
  restates `alpha=0`.
