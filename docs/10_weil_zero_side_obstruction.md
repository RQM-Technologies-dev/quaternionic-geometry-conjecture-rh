# Weil Zero-Side Obstruction

This note expands the zero-side term for the Candidate v0 Weil test family from
[09_candidate_v0_weil_test_family.md](09_candidate_v0_weil_test_family.md). It
is an obstruction audit for Lemma C: it identifies what the test family must
control before it can turn an off-line zero into a contradiction with the
Bombieri-Weil sign condition.

## Setup

Use the same parameters as the test-family note:

```text
rho0 = 1/2 + alpha + i t,
alpha != 0,
```

where `rho0` is an assumed off-line zero. The additive profile is

```text
h_{alpha,t}(u)
= h0_{alpha,t}(u) - a_{alpha,t} e0(u) - b_{alpha,t} e1(u),
```

with

```text
h0_{alpha,t}(u) = E(u) exp(i t u) sinh(alpha u),
e0(u) = E(u),
e1(u) = u E(u).
```

The positive-half-line test function is

```text
g_{alpha,t}(x) = h_{alpha,t}(log x),
```

and the autocorrelation is

```text
f_{alpha,t}(x)
= integral_0^infinity g_{alpha,t}(x y) g_{alpha,t}(y) dy.
```

## Envelope Transform

Introduce the envelope Mellin-Laplace transform

```text
K(z) = integral_R E(u) exp(z u) du.
```

Formally,

```text
K'(z) = integral_R u E(u) exp(z u) du.
```

Since `E` is even, the transform has the parity identities

```text
K(-z) = K(z),
K'(-z) = -K'(z),
```

inside the common strip where the integrals are valid. The rapid theta-kernel
decay from the previous note is the analytic input needed to justify these
evaluations on the shifted lines used below.

## Mellin Transform Of The Seed

For

```text
G_{alpha,t}(s)
= tilde_g_{alpha,t}(s)
= integral_0^infinity g_{alpha,t}(x) x^s dx / x,
```

the additive variable gives

```text
G_{alpha,t}(s) = integral_R h_{alpha,t}(u) exp(s u) du.
```

The raw seed contributes

```text
G0_{alpha,t}(s)
= integral_R E(u) exp((s + i t)u) sinh(alpha u) du
= (1/2) { K(s + i t + alpha) - K(s + i t - alpha) }.
```

The centered profile therefore has

```text
G_{alpha,t}(s)
= G0_{alpha,t}(s)
  - a_{alpha,t} K(s)
  - b_{alpha,t} K'(s).
```

The centering coefficients are fixed by

```text
G_{alpha,t}(0) = 0,
G_{alpha,t}(1) = 0.
```

Because `K'(0)=0`, the coefficients can be written as

```text
a_{alpha,t} = G0_{alpha,t}(0) / K(0),

b_{alpha,t}
= { G0_{alpha,t}(1) - a_{alpha,t} K(1) } / K'(1),
```

provided `K(0)` and `K'(1)` are nonzero, as checked by the positivity argument
in the test-family note.

## Endpoint Terms Vanish

The Bombieri-Weil explicit formula in
[08_weil_formula_transcription.md](08_weil_formula_transcription.md) has

```text
W_B(f) = tilde_f(0) - sum_rho tilde_f(rho) + tilde_f(1).
```

For the autocorrelation family,

```text
tilde_f_{alpha,t}(s)
= G_{alpha,t}(s) G_{alpha,t}(1-s).
```

The two Bombieri normalization constraints give

```text
G_{alpha,t}(0) = 0,
G_{alpha,t}(1) = 0.
```

Thus

```text
tilde_f_{alpha,t}(0) = 0,
tilde_f_{alpha,t}(1) = 0,
```

and the sign question is entirely a zero-side question:

```text
W_B(f_{alpha,t})
= - sum_rho G_{alpha,t}(rho) G_{alpha,t}(1-rho).
```

To force a Bombieri-sign violation from an off-line zero, the needed theorem is
therefore:

```text
rho0 = 1/2 + alpha + i t is a zero and alpha != 0
  => sum_rho G_{alpha,t}(rho) G_{alpha,t}(1-rho) < 0.
```

This is stronger than showing that the selected zero gives a nonzero term.

## Selected Zero Contribution

At the selected zero

```text
rho0 = 1/2 + alpha + i t,
```

the raw factor is

```text
G0_{alpha,t}(rho0)
= (1/2) {
    K(1/2 + 2 alpha + 2 i t)
    - K(1/2 + 2 i t)
  }.
```

At the reflected point

```text
1 - rho0 = 1/2 - alpha - i t,
```

the raw factor is

```text
G0_{alpha,t}(1-rho0)
= (1/2) {
    K(1/2)
    - K(1/2 - 2 alpha)
  }.
```

After centering, the actual selected contribution is

```text
G_{alpha,t}(rho0) G_{alpha,t}(1-rho0)
= {
    G0_{alpha,t}(rho0)
    - a_{alpha,t} K(rho0)
    - b_{alpha,t} K'(rho0)
  }
  {
    G0_{alpha,t}(1-rho0)
    - a_{alpha,t} K(1-rho0)
    - b_{alpha,t} K'(1-rho0)
  }.
```

This is the first obstruction: the selected off-line zero does not contribute a
bare Candidate v0 expression. It contributes a centered expression whose two
projection corrections may be the same size as the raw mirror-imbalance term.

## Zero-Orbit Contribution

An off-line zero would occur with its symmetry orbit:

```text
rho0, 1-rho0, conjugate(rho0), 1-conjugate(rho0).
```

The zero side therefore contains at least the orbit sum

```text
Z_orbit(alpha,t)
= G(rho0) G(1-rho0)
  + G(1-rho0) G(rho0)
  + G(conjugate(rho0)) G(1-conjugate(rho0))
  + G(1-conjugate(rho0)) G(conjugate(rho0)).
```

Equivalently,

```text
Z_orbit(alpha,t)
= 2 G(rho0) G(1-rho0)
  + 2 G(conjugate(rho0)) G(1-conjugate(rho0)).
```

The full zero sum is still larger:

```text
sum_rho G(rho) G(1-rho)
= Z_orbit(alpha,t) + Z_rest(alpha,t),
```

where `Z_rest(alpha,t)` is the contribution from every other nontrivial zero.

The desired contradiction requires

```text
Z_orbit(alpha,t) + Z_rest(alpha,t) < 0.
```

This is the second obstruction: Candidate v0 has not yet supplied a localization
or dominance theorem controlling `Z_rest(alpha,t)`.

## Sign Obstruction

With the current Candidate v0 attachment, there are three unresolved sign
issues.

1. The centered selected term

```text
G(rho0) G(1-rho0)
```

has no fixed sign from the construction alone.

2. The orbit sum

```text
Z_orbit(alpha,t)
```

has no established sign after the reflected and conjugate terms are combined.

3. Even if the orbit sum had the favorable sign, the remaining zero contribution

```text
Z_rest(alpha,t)
```

could cancel it unless a separate localization, positivity, or domination
estimate is proved.

Therefore the present test family reaches the Weil machinery, but it does not
yet close Lemma C.

## Consequence For Candidate v0

Candidate v0 remains useful as an axis detector:

```text
S_Xi(s)=0  iff  Re(s)=1/2.
```

The Weil calculation shows that this is not yet enough to prove

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

To make Lemma C viable, the next construction must add one of the following:

- a localization theorem showing `G_{alpha,t}` isolates the off-line zero orbit;
- a domination theorem bounding `Z_rest(alpha,t)` by the selected orbit term;
- a strengthened explicit-formula energy whose sign is tied directly to
  `S_Xi(s)` or to a monotone transform of it.

## Next Work Item

The next note should test the third option:

```text
docs/11_weil_energy_strengthening.md
```

It should ask whether Candidate v0 should be replaced by, or embedded into, a
Weil-native quadratic energy

```text
E_Weil(alpha,t) = -W_B(f_{alpha,t})
```

or into a localized variant that has an explicit zero-orbit dominance theorem.
