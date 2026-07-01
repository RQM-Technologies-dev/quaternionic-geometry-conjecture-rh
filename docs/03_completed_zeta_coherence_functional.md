# Completed-Zeta Coherence Functional

This document defines the central research target: a completed-zeta coherence
functional whose scale-stable cancellation axis is `Re(s)=1/2`.

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

## Quaternionic Completed Target

The quaternionic completed target is

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
- `C_QF_RH(q)` is the candidate shell/coherence surface.
- On a fixed admissible slice, `Xi_H(q)` should reduce to the classical
  completed-zeta expression after projection.

Off-slice, `Xi_H(q)` remains a research target until `Gamma_H`, `Z_H`, branch
choices, multiplication order, and functional calculus are fixed.

## Desired Coherence Property

The desired theorem-level shape is:

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
| Slice completed-zeta residual | Checks `Xi(s)`, projection, and reflection conventions | Zero detection, because exact `Xi(s)=Xi(1-s)` already vanishes as a residual |
| Gamma-lift conjugacy defect | Tests branch/domain behavior of `Gamma_H` | A zeta-zero link without `Z_H` and completed structure |
| Weil/explicit-formula energy | Best long-term route toward positivity/coercivity | RH consequence until connected to a known criterion non-circularly |

The main object is `C_QF_RH(q)`. Supporting diagnostics should serve that
object rather than multiply independent proof routes.

## Zero Shells And Completion Weights

If `t_n` is a positive ordinate of a nontrivial zero, the diagnostic shell is

```text
q_n(u) = 1/2 + t_n u.
```

The completed object evaluates the Gamma/factorial envelope on that shell. This
does not mean Gamma generates the zero. It means the zero shell is studied
inside the completed mirror geometry.

Known `t_n` values may be used only after the functional is defined, and only
to test whether diagnostics reproduce expected shell behavior.

## Proof-Weight Requirements

Before `C_QF_RH(q)` can carry theorem weight, the program must specify:

- the domain of `q`;
- the admissible slice family;
- `Gamma_H(q)` and `Z_H(q)`;
- branch and multiplication-order conventions;
- the norm or energy structure;
- the stationarity, positivity, or coercivity condition;
- the implication direction connecting the condition to zeros.

Without these, `C_QF_RH(q)` is a research target and diagnostic organizer.
