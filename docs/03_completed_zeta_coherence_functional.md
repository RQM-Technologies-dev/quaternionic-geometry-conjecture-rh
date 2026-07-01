# Completed-Zeta Coherence Functional

This document defines the central research target: first a classical
completed-zeta scale-stability defect `S_Xi(s)`, then a quaternionic lift of
that target.

The target is conjectural. It is not a proof of RH.

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

## Classical Core

The immediate target is a real-valued scale-stability defect

```text
S_Xi(s).
```

This is not yet a finished formula. It is the planned classical object that
must be built from:

- the completed zeta function `Xi(s)`,
- the reflection `s -> 1-s`,
- an admissible log-scale or test-function structure,
- a norm, energy, or stress interpretation stated before diagnostics.

`S_Xi(s)` must not use known zero locations, tabulated ordinates, or tuning
against numerical zero data.

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

Before `S_Xi(s)` can carry theorem weight, the program must specify:

- its domain in the critical strip or completed-zeta domain;
- the admissible log-scale or test-function class;
- the norm, energy, or stress interpretation;
- the off-axis coercivity statement `S_Xi(s)=0 => Re(s)=1/2`;
- the zero-to-stability statement `Xi(s)=0 => S_Xi(s)=0`.

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
