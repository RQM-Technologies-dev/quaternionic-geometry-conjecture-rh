# Completed Zeta Stability

This repository is `completed-zeta-stability`: a compact, claim-disciplined
research program for the **Completed Zeta Stability Conjecture**.

The target is narrow:

```text
Build a non-circular completed-zeta stability functional for which Re(s)=1/2
is the only scale-stable cancellation axis.
```

The conjecture asks whether a completed-zeta scale-stability defect `S_Xi(s)`
can be defined so that

```text
Xi(s)=0  =>  S_Xi(s)=0  =>  Re(s)=1/2.
```

The current Candidate v0 supplies the completed scale measure and the
mirror-axis uniqueness result. The remaining proof-level gap is Lemma C,
`Xi(s)=0 => S_Xi(s)=0`.

## Direction

```text
completed theta kernel
  -> positive completed scale measure mu_Xi
  -> Candidate v0 scale-stability defect S_Xi
  -> Lemma B: S_Xi(s)=0 => Re(s)=1/2
  -> Lemma C: Xi(s)=0 => S_Xi(s)=0
  -> optional quaternionic lift only after the classical bridge is proved
```

## Current Documents

- `CLAIM_DISCIPLINE.md` keeps the framing conjectural and obligation-first.
- `ROADMAP.md` gives the short proof-route development path.
- `docs/01_definition_ledger.md` records canonical notation, assumptions, and
  non-circularity rules.
- `docs/02_candidate_v0_core.md` consolidates the conjecture target, Lemma A,
  Candidate v0, and Lemma B.
- `docs/03_lemma_c_weil_bridge.md` is the active Lemma C Weil-positivity bridge
  and coefficient/tail estimate target.
- `docs/references.md` lists the background sources and analytic targets.
- `references/bombieri-riemann-hypothesis-millennium.pdf` is the local source
  copy of Bombieri's Millennium problem article.

## Read Next

- [CLAIM_DISCIPLINE.md](CLAIM_DISCIPLINE.md) - public framing rules.
- [ROADMAP.md](ROADMAP.md) - focused proof-route sequence.
- [docs/01_definition_ledger.md](docs/01_definition_ledger.md) - notation and
  non-circularity ledger.
- [docs/02_candidate_v0_core.md](docs/02_candidate_v0_core.md) - Candidate v0,
  Lemma A, and Lemma B.
- [docs/03_lemma_c_weil_bridge.md](docs/03_lemma_c_weil_bridge.md) - active
  Lemma C bridge and next estimate target.
- [references/bombieri-riemann-hypothesis-millennium.pdf](references/bombieri-riemann-hypothesis-millennium.pdf) -
  local copy of the original problem article used by the Weil bridge.

## Checks

```bash
python scripts/check_markdown_links.py
python scripts/smoke.py
```
