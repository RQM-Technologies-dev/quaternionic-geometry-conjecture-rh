# Weil Formula Transcription

This note locks the explicit-formula convention needed before any Candidate v0
bridge attempt. It is a transcription and bridge audit, not a proof of the
Riemann Hypothesis.

Local source copy:
[bombieri-riemann-hypothesis-millennium.pdf](../references/bombieri-riemann-hypothesis-millennium.pdf).

## Test-Function Class

Following Bombieri's notation, let `W` be the class of complex-valued functions
`f(x)` on the positive half-line such that:

- `f` is continuous and continuously differentiable except at finitely many
  points;
- at each exceptional point, `f` and `f'` have at most a jump discontinuity and
  are assigned the average of their left and right limits;
- for some `delta > 0`,

```text
f(x) = O(x^delta)        as x -> 0+,
f(x) = O(x^(-1-delta))  as x -> infinity.
```

Use the Mellin-transform convention

```text
tilde_f(s) = integral_0^infinity f(x) x^s dx / x.
```

Then `tilde_f(s)` is analytic in the strip

```text
-delta < Re(s) < 1 + delta.
```

## Bombieri-Weil Explicit Formula

Let `Lambda(n)` be the von Mangoldt function:

```text
Lambda(n) = log p  if n = p^a for a prime p and integer a >= 1,
Lambda(n) = 0      otherwise.
```

For `f in W`, Bombieri states Weil's explicit formula for the Riemann zeta
function as

```text
tilde_f(0) - sum_rho tilde_f(rho) + tilde_f(1)
=
sum_{n>=1} Lambda(n) { f(n) + (1/n) f(1/n) }
+ (log(4*pi) + gamma) f(1)
+ integral_1^infinity
    { f(x) + (1/x) f(1/x) - (2/x) f(1) }
    dx / (x - x^(-1)).
```

The zero sum runs over all nontrivial zeros `rho` of `zeta(s)` and is
understood as

```text
lim_{T -> infinity} sum_{|Im(rho)| < T} tilde_f(rho).
```

For this repo, call the right-hand side

```text
W_B(f).
```

The subscript `B` means this note is using Bombieri's sign convention.

## Weil Positivity Criterion

Bombieri records that RH is equivalent to negativity of the right-hand side for
all functions of the form

```text
f(x) = integral_0^infinity g(x y) g(y) dy,
```

where `g in W` satisfies

```text
integral_0^infinity g(x) dx / x = 0,
integral_0^infinity g(x) dx = 0.
```

In this sign convention, the proof target is:

```text
W_B(f) <= 0
```

for every admissible `f` of this autocorrelation form. This is the
Weil-positivity problem in Bombieri's wording: a sign theorem for the explicit
formula replaces direct zero hunting.

## Lemma C Reformulation

The repo's Lemma C is

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

Using Lemma B, Candidate v0 has

```text
S_Xi(s)=0  iff  Re(s)=1/2.
```

Thus, for Candidate v0, Lemma C can be attacked through the following
Weil-positivity reformulation:

```text
Assume an off-line zero rho = 1/2 + alpha + i t with alpha != 0.
Construct an admissible f_{alpha,t} in the Weil test class.
Show that this off-line zero forces W_B(f_{alpha,t}) > 0.
Prove independently that W_B(f) <= 0 for all admissible f.
Conclude no such off-line zero exists.
Therefore alpha = 0 and S_Xi(rho)=0.
```

This is the explicit-formula version of the desired bridge:

```text
Xi(s)=0
  -> violation/equality condition in a Weil quadratic form
  -> Candidate v0 scale-stability
  -> S_Xi(s)=0.
```

## Candidate v0 Attachment Test

Candidate v0 lives on the log-scale variable `y`:

```text
x = exp(y),
s = 1/2 + alpha + i t,
M(alpha) = integral_R exp(2 alpha y) dmu_Xi(y),
S_Xi(s) = 1 - 1 / (M(alpha) M(-alpha)).
```

The Weil formula lives on the positive half-line variable `x`, with Mellin
transform `tilde_f(s)`. The natural dictionary is:

```text
y = log x,
exp(alpha y) = x^alpha,
exp(i t y) = x^(i t).
```

A Candidate v0 attachment must therefore turn the mirror scale profiles

```text
exp(alpha y), exp(-alpha y)
```

and the oscillatory zero profile

```text
exp(i t y)
```

into an admissible `g`, or into an admissible autocorrelation

```text
f(x) = integral_0^infinity g(x y) g(y) dy.
```

This cannot be done by using the raw profiles alone: they do not satisfy the
decay and normalization requirements of the Weil test class. Any valid
attachment must add a completed envelope, cutoff, projection, or centering step
before applying the explicit formula.

## Audit Outcomes

Outcome A: Candidate v0 attaches.

```text
S_Xi(s), or a monotone transform of it, is represented by, bounded by, or
strengthened into an admissible Weil quadratic form W_B(f_{alpha,t}).
```

This would give a concrete route to Lemma C after a sign theorem is proved.

Outcome B: Candidate v0 is too weak.

```text
S_Xi(s) detects only alpha and does not produce an admissible Weil quadratic
form that sees oscillatory cancellation at t.
```

Then Candidate v0 remains useful as the Lemma A/B axis detector, but Lemma C
requires a strengthened explicit-formula energy that sees both:

```text
scale imbalance alpha,
oscillatory cancellation at height t.
```

## Active Test-Family Note

The first admissible test-family candidate is:

```text
docs/09_candidate_v0_weil_test_family.md
```

It builds a centered, decaying `g_{alpha,t}` from the theta-kernel envelope and
mirror profiles, verifies the two Bombieri normalization constraints, and states
what `W_B(f_{alpha,t})` would need to control.
