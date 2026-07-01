# Roadmap

This roadmap keeps the repository pointed at one research target: a rigorous
completed-zeta coherence functional where `Re(s)=1/2` is the only scale-stable
cancellation axis.

## 1. Lock Definitions

- Use [docs/01_definition_ledger.md](docs/01_definition_ledger.md) as the
  canonical source for `s`, `q`, slices, reflections, norms, `Xi`, `S_Xi`,
  `Gamma_H`, `Z_H`, and non-circularity rules.
- Treat off-slice `Gamma_H`, `Z_H`, multiplication order, and functional
  calculus as analytic development targets until explicitly constructed.
- Do not introduce diagnostics that depend on choices missing from the ledger.

## 2. Establish The Mirror-Scaling Axis

- Use [docs/02_mirror_scaling_eigenring.md](docs/02_mirror_scaling_eigenring.md)
  to keep the central algebra visible: local prime mirror amplitudes
  `p^(-sigma)` and `p^(-(1-sigma))` match iff `sigma=1/2`.
- Develop this as a scale-stability target, not as a naive Euler-product proof
  in the critical strip.
- Keep EigenRing geometry as an invariance lemma for shells already on the
  critical slice.

## 3. Define The Classical Scale-Stability Core

- Use [docs/03_completed_zeta_coherence_functional.md](docs/03_completed_zeta_coherence_functional.md)
  as the canonical target document.
- Make `S_Xi(s)` the immediate milestone: a real-valued completed-zeta
  scale-stability defect defined before any quaternionic lift.
- Organize the proof target as the bridge lemma program: completion transport
  for `mu_Xi`, mirror-axis uniqueness for `S_Xi`, then the hard
  zero-to-stability bridge.
- Treat `Xi_H(q)` and `C_QF_RH(q)=||Xi_H(q)||^2` as the quaternionic extension
  of the classical core.
- Treat slice checks, Gamma-lift conjugacy, and Weil/explicit-formula energy as
  supporting tests for the completed target, not as separate proof paths.

## 4. Prove Obligations Before Diagnostics

- Use [docs/04_theorem_obligations_and_diagnostics.md](docs/04_theorem_obligations_and_diagnostics.md)
  to separate theorem obligations from numerical checks.
- State the stationarity-to-zero implication before using zero data.
- Use known zero ordinates only after definitions are fixed, and only as
  diagnostics.
