# Theorem Obligations And Diagnostics

This document separates what must be proved from what may be checked
numerically.

## Theorem-Level Obligations

The program needs the following obligations before any RH-relevant claim can
carry proof weight.

1. Define the analytic domain for `Xi_H(q)`.
2. Construct `Gamma_H(q)` on that domain or restrict the claim to fixed slices.
3. Define `Z_H(q)` and prove slice compatibility with the classical zeta side.
4. Fix branch choices and multiplication order for all noncommutative factors.
5. Define the norm, energy, or stress functional used by `C_QF_RH(q)`.
6. State the stationarity, positivity, or coercivity condition before using
   zero data.
7. Prove the implication direction: zero to stationarity, stationarity to zero,
   or equivalence.
8. Establish off-axis control strong enough to rule out scale-stable
   cancellation away from `Re(s)=1/2`.

## Diagnostic Rules

Known zeta-zero data is useful only after the analytic object is fixed.

Allowed diagnostic uses:

- verify projection conventions on the critical line;
- compare shell radii `|Im(q)|` with known ordinates `t_n`;
- check numerical residuals for branch, normalization, and reflection errors;
- test whether candidate stationarity conditions are stable under slice
  changes;
- compare candidate energy signs with known explicit-formula expectations.

Forbidden diagnostic uses:

- defining the functional from the known zero list;
- tuning norms, branches, or slices until known zeros appear;
- treating numerical agreement as theorem evidence;
- claiming a quaternionic visualization proves zero confinement.

## Acceptance Standard For New Theory Text

Any new theory note must state:

- which parts are classical;
- which parts are definitions;
- which parts are diagnostics;
- which parts are conjectural;
- what theorem-level obligation would make the claim proof-weighted.

## Minimal Future Diagnostic Output

If diagnostic scripts are added later, they should produce:

- the exact definitions used for `Xi_H` or the chosen slice restriction;
- a manifest of zero data sources;
- residual and symmetry-error summaries;
- stationarity or energy measurements;
- a statement that outputs are diagnostic only.

No diagnostic should be introduced until the corresponding analytic definition
is recorded in the ledger.
