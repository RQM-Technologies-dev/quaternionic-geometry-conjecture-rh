# Roadmap

This roadmap keeps `completed-zeta-stability` pointed at one proof route: build
and test a completed-zeta stability defect whose stable axis is `Re(s)=1/2`.

## 1. Keep The Definitions Fixed

- Use [docs/01_definition_ledger.md](docs/01_definition_ledger.md) as the
  canonical source for `s`, `q`, reflections, `Xi`, `Phi_Xi`, `mu_Xi`,
  `M(alpha)`, `S_Xi`, and non-circularity rules.
- Keep quaternionic objects downstream of the classical completed-zeta target.
- Do not add diagnostics or visual language that changes the theorem
  obligation.

## 2. Preserve Candidate v0 As The Core

- Use [docs/02_candidate_v0_core.md](docs/02_candidate_v0_core.md) as the
  compact proof-route core.
- Lemma A supplies the positive completed scale measure from the theta kernel.
- Lemma B proves Candidate v0 mirror-axis uniqueness:

```text
S_Xi(s)=0  =>  Re(s)=1/2.
```

- Do not re-open mirror-scaling or EigenRing side routes unless they strengthen
  Lemma C.

## 3. Work Only On Lemma C

- Use [docs/03_lemma_c_weil_bridge.md](docs/03_lemma_c_weil_bridge.md) as the
  active bridge document.
- The theorem-level gap is:

```text
Xi(s)=0  =>  S_Xi(s)=0.
```

- The next proof task is the coefficient/tail estimate for the Gaussian-window
  Weil family: bound the centering coefficients, prove selected-orbit
  non-cancellation, and control `Z_rest`.
- Treat the EigenCircle critical-slice language only as an interpretation of
  selected-orbit survival unless it is derived from the Weil machinery.

## 4. Keep The Repo Small

- Add new numbered docs only when they become canonical proof-route documents.
- Do not archive exploratory notes in this repo.
- Use known zero ordinates only as diagnostics after the analytic object is
  fixed.
