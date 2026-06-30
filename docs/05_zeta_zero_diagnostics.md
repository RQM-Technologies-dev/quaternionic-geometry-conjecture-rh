# Zeta Zero Diagnostics

Known zeta-zero data is useful as a diagnostic target for the conjecture
program.

The diagnostic role is narrow and important: zero data can test whether a
candidate spectral-coherence functional has the expected critical-line
geometry, symmetry behavior, and residual pattern.

## Diagnostic Uses

Use zero data to check:

- whether projected stationary states lie on `Re(s)=1/2`,
- whether conjugate symmetry produces matched pairs,
- whether residuals concentrate near expected zero ordinates,
- whether off-slice probes create coherence defects,
- whether normalization choices shift or stabilize the diagnostics.

## Suggested Outputs

Future diagnostic scripts should produce:

- a manifest describing the chosen zeta-zero source,
- parameters for the quaternionic lift and coherence functional,
- projected stationary-state locations,
- residual and symmetry-error summaries,
- figures comparing the critical line with the critical slice projection.

## Interpretation Standard

Numerical diagnostics guide analytic target selection. The public interpretation
should remain:

```text
zero data -> diagnostic comparison -> analytic development target
```

