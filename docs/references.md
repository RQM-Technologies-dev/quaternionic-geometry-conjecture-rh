# References

This repository is the Completed Zeta Stability Conjecture program. The
references below mark the classical, positivity, and quaternionic background
that should inform the completed-zeta stability target.

## Classical Zeta Theory

- Bernhard Riemann, "On the Number of Primes Less Than a Given Magnitude"
  (1859).
- E. Bombieri, "Problems of the Millennium: the Riemann Hypothesis".
  Local copy: [bombieri-riemann-hypothesis-millennium.pdf](../references/bombieri-riemann-hypothesis-millennium.pdf).
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*.
- H. M. Edwards, *Riemann's Zeta Function*.
- H. Iwaniec and E. Kowalski, *Analytic Number Theory*.
- J. B. Conrey, "The Riemann Hypothesis", *Notices of the AMS*.

## Explicit-Formula And Positivity Background

- Andre Weil, explicit-formula positivity criteria for zeta and L-functions.
- Riemann's theta-kernel / Fourier-cosine representation of the completed
  xi function.
- A. M. Odlyzko, computational studies of zeta zeros and zero statistics.
- E. Bombieri, survey writing on the Riemann zeta function and the Riemann
  Hypothesis.

## Quaternionic And Slice-Analytic Background

- R. Fueter, early quaternionic analysis.
- G. Gentili and D. C. Struppa, slice-regular quaternionic function theory.
- F. Colombo, I. Sabadini, and D. C. Struppa, quaternionic functional calculus
  and slice-hyperholomorphic methods.

## Repository-Specific Development Targets

- Define the classical scale-stability defect `S_Xi(s)` precisely.
- Lift `S_Xi(s)` only afterward through `Xi_H(q)` and `C_QF_RH(q)`.
- Connect the mirror-scaling identity to a legitimate completed-zeta or
  explicit-formula object.
- Use the Bombieri/Weil explicit-formula route as the next Lemma C bridge audit.
- State a non-circular stationarity, positivity, or coercivity condition.
- Use zero data only as diagnostics after the analytic object is fixed.
