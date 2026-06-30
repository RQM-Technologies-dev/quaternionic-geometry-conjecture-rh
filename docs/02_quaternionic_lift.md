# Quaternionic Lift

The quaternionic lift is the first analytic development target. It supplies the
space in which the classical zeta symmetry can be reinterpreted geometrically.

## Quaternionic Variable

Write

```text
q = a + b i + c j + d k.
```

The real part is `a`. The imaginary part is the vector component
`b i + c j + d k`.

A complex slice is obtained by choosing a unit imaginary quaternion `u` and
restricting to

```text
q = a + t u.
```

This gives a complex plane inside the quaternionic algebra.

## Gamma-Lift Target

The guiding lift is a quaternionic factorial/Gamma object:

```text
Gamma_H(q) = integral_0^infinity exp(-x) exp(q log x) dx.
```

On a fixed complex slice, this should reduce to the corresponding complex
Gamma-type continuation after compatible branch and domain choices are made.

## Development Questions

The lift must answer:

- Which quaternionic domain is used?
- Which slice-regular or slice-compatible framework is assumed?
- How are branches chosen for logarithmic terms?
- How does multiplication order affect the lifted functional equation?
- Which normalization corresponds to the completed zeta function?
- Which symmetry is exact, and which is part of the conjectural model?

## Minimum Standard

The lift should be explicit enough that later documents can state exactly what
`C(q)` depends on, how conjugation acts, and how the complex critical line is
recovered by slice projection.

