# Theorem Obligations And Diagnostics

This document separates what must be proved from what may be checked
numerically.

## Theorem-Level Obligations

The program needs the following obligations before any RH-relevant claim can
carry proof weight.

1. Define `S_Xi(s)` precisely as a real-valued completed-zeta scale-stability
   defect. Candidate v0 is the completed mirror-angle defect.
2. State its construction domain, completed kernel `Phi_Xi`, normalized
   measure `mu_Xi`, and admissible moment range.
3. Make `S_Xi(s)` account for the full completed envelope `A(s) zeta(s)`, not
   only local prime amplitudes.
4. Prove Lemma A, completion transport:

   ```text
   Gamma/pi completion -> Phi_Xi -> mu_Xi.
   ```

   This must establish the positivity, finiteness, non-degeneracy, and moment
   assumptions needed by Candidate v0. Quaternionic Gamma/factorial geometry
   may interpret this transport after the classical completed kernel is fixed,
   but it must not generate zeros or define the measure from zero data.

5. Prove Lemma B, off-axis coercivity:

   ```text
   S_Xi(s) = 0  =>  Re(s)=1/2.
   ```

   For Candidate v0, this is expected to follow from Cauchy-Schwarz plus
   positivity, finiteness, and non-degeneracy of `mu_Xi`.

6. Prove Lemma C, the zero-to-stability bridge:

   ```text
   Xi(s) = 0  =>  S_Xi(s)=0.
   ```

   This is the hard RH-level theorem target.

7. Combine Lemma A, Lemma B, and Lemma C to conclude that all nontrivial zeros
   in the intended domain lie on `Re(s)=1/2`.
8. Only after the classical core is defined, construct the optional
   quaternionic lift `Xi_H(q)` and `C_QF_RH(q)`.
9. For the lift, define `Gamma_H(q)`, `Z_H(q)`, branch choices,
   multiplication order, norm, and slice compatibility.
10. State any stationarity, positivity, or coercivity condition before using
   zero data.
11. Establish off-axis control strong enough to rule out scale-stable
   cancellation away from `Re(s)=1/2`.

## Diagnostic Rules

Known zeta-zero data is useful only after the analytic object is fixed.

Allowed diagnostic uses:

- verify projection conventions on the critical line;
- compare shell radii `|Im(q)|` with known ordinates `t_n`;
- check numerical residuals for branch, normalization, and reflection errors;
- test candidate formulas for `S_Xi(s)` after the formula is fixed;
- test whether candidate stationarity conditions are stable under slice
  changes;
- compare candidate energy signs with known explicit-formula expectations.

Forbidden diagnostic uses:

- defining the functional from the known zero list;
- defining `S_Xi(s)` so that it vanishes exactly at tabulated ordinates;
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

- the exact definitions used for `S_Xi`, `Xi_H`, or the chosen slice
  restriction;
- a manifest of zero data sources;
- residual and symmetry-error summaries;
- stationarity or energy measurements;
- a statement that outputs are diagnostic only.

No diagnostic should be introduced until the corresponding analytic definition
is recorded in the ledger.
