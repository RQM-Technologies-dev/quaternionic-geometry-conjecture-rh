# Candidate v0 Weil Test Family

This note constructs the first admissible Weil test-family candidate attached to
Candidate v0. It is a bridge audit, not a proof of Lemma C or the Riemann
Hypothesis.

The goal is to test whether the Candidate v0 scale-stability defect can be
connected to the Bombieri-Weil explicit-formula sign condition recorded in
[08_weil_formula_transcription.md](08_weil_formula_transcription.md).

## Target

Candidate v0 has:

```text
s = 1/2 + alpha + i t,
M(alpha) = integral_R exp(2 alpha u) dmu_Xi(u),
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

Lemma B proves:

```text
S_Xi(s)=0  iff  alpha=0.
```

Lemma C asks for:

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

The Weil route tests whether an off-line zero can be converted into a violation
of the Bombieri-Weil sign condition:

```text
W_B(f) <= 0
```

for admissible autocorrelation test functions.

## Additive Variable

Use the additive log-scale variable

```text
u = log x.
```

If `g(x)` is a positive-half-line test function, write

```text
h(u) = g(exp u).
```

The two Bombieri normalization constraints become:

```text
integral_0^infinity g(x) dx / x = integral_R h(u) du = 0,
integral_0^infinity g(x) dx     = integral_R exp(u) h(u) du = 0.
```

Thus an admissible Candidate v0 attachment must satisfy two additive moment
constraints:

```text
L0(h) = integral_R h(u) du = 0,
L1(h) = integral_R exp(u) h(u) du = 0.
```

## Completed Envelope

Let `Phi_Xi(u)` be the positive even theta kernel from the Lemma A note, and set

```text
E(u) = sqrt(Phi_Xi(u)).
```

The theta-kernel decay gives rapid decay for `E(u)` and for polynomial or
exponential tilts of `E(u)` over any fixed real `alpha`. This envelope is the
first safeguard against using raw profiles that are not in the Weil test class.

## Raw Candidate Seed

For real `alpha` and real `t`, define the raw additive seed

```text
h0_{alpha,t}(u)
= E(u) exp(i t u) sinh(alpha u).
```

This seed has the intended ingredients:

- `E(u)` supplies completed theta-kernel decay;
- `exp(i t u)` records the oscillatory zero height;
- `sinh(alpha u)` records mirror scale imbalance and vanishes when `alpha=0`.

The seed is not yet admissible, because it need not satisfy `L0=0` and `L1=0`.

## Centering Projection

Use two fixed correction directions:

```text
e0(u) = E(u),
e1(u) = u E(u).
```

Since `E` is positive and even,

```text
L0(e0) > 0,
L0(e1) = 0,
L1(e0) > 0,
L1(e1) = integral_R u exp(u) E(u) du > 0.
```

The last inequality follows because

```text
integral_R u exp(u) E(u) du = integral_R u sinh(u) E(u) du,
```

and `u sinh(u) >= 0`, not identically zero. Therefore the `2 x 2` moment matrix
for `e0,e1` is invertible.

Choose coefficients `a_{alpha,t}` and `b_{alpha,t}` so that

```text
h_{alpha,t}(u)
= h0_{alpha,t}(u) - a_{alpha,t} e0(u) - b_{alpha,t} e1(u)
```

satisfies

```text
L0(h_{alpha,t}) = 0,
L1(h_{alpha,t}) = 0.
```

Explicitly, solve

```text
[ L0(e0)  L0(e1) ] [ a_{alpha,t} ] = [ L0(h0_{alpha,t}) ]
[ L1(e0)  L1(e1) ] [ b_{alpha,t} ]   [ L1(h0_{alpha,t}) ].
```

This produces a centered, rapidly decaying additive test profile.

## Positive-Half-Line Test Function

Define

```text
g_{alpha,t}(x) = h_{alpha,t}(log x).
```

Then `g_{alpha,t}` satisfies the two Bombieri normalization constraints:

```text
integral_0^infinity g_{alpha,t}(x) dx / x = 0,
integral_0^infinity g_{alpha,t}(x) dx = 0.
```

Because the theta envelope decays rapidly at both ends in the additive variable,
`g_{alpha,t}` has the endpoint decay required for the Weil class for fixed
`alpha,t`. If a fully formal proof is needed later, it should state the
allowed compact `alpha,t` ranges and the inherited smoothness of `Phi_Xi`.

## Autocorrelation Test Function

Define the Bombieri-Weil autocorrelation

```text
f_{alpha,t}(x)
= integral_0^infinity g_{alpha,t}(x y) g_{alpha,t}(y) dy.
```

For this convention, the Mellin transform factors as

```text
tilde_f_{alpha,t}(s)
= tilde_g_{alpha,t}(s) tilde_g_{alpha,t}(1-s),
```

where

```text
tilde_g_{alpha,t}(s)
= integral_0^infinity g_{alpha,t}(x) x^s dx / x.
```

This factorization is the main reason the test family is relevant to Lemma C:
zeros enter the explicit formula through

```text
tilde_f_{alpha,t}(rho)
= tilde_g_{alpha,t}(rho) tilde_g_{alpha,t}(1-rho).
```

An off-line reflected pair has

```text
rho = 1/2 + alpha + i t,
1-rho = 1/2 - alpha - i t.
```

Thus the Weil test family can see both the scale imbalance `alpha` and the
oscillatory height `t`.

## What Must Be Controlled

With Bombieri's sign convention, the desired sign theorem is:

```text
W_B(f_{alpha,t}) <= 0
```

for every admissible `f_{alpha,t}`. To turn this into Lemma C, the test family
would need the following implication:

```text
rho = 1/2 + alpha + i t is a zero and alpha != 0
  => W_B(f_{alpha,t}) > 0.
```

Together these would rule out `alpha != 0`, hence force `S_Xi(rho)=0` by Lemma
B.

## Attachment Audit

This construction succeeds at the admissibility level:

- it supplies completed-kernel decay through `E(u)`;
- it includes the mirror imbalance `sinh(alpha u)`;
- it includes the zero height through `exp(i t u)`;
- it enforces the two Bombieri normalization constraints by projection;
- it produces an autocorrelation with Mellin factorization.

It does not yet prove the required sign implication. The open calculation is:

```text
Can W_B(f_{alpha,t}) be bounded below by a positive expression when
rho = 1/2 + alpha + i t is an off-line zero?
```

If yes, Candidate v0 has a concrete Weil-positivity bridge.

If no, Candidate v0 remains an axis detector, and Lemma C requires a stronger
explicit-formula energy whose definition is built directly from `W_B`.

## Active Obstruction Note

The zero-side obstruction for this family is expanded in:

```text
docs/10_weil_zero_side_obstruction.md
```

That note expands

```text
tilde_f_{alpha,t}(rho)
= tilde_g_{alpha,t}(rho) tilde_g_{alpha,t}(1-rho)
```

for the centered profile above and identify whether an off-line zero forces a
positive contribution to `W_B(f_{alpha,t})`, or whether cancellation from the
remaining zeros prevents a Lemma C conclusion.
