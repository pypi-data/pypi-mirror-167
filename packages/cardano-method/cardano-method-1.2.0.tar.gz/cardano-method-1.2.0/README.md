
# cardano-method

[![release](https://img.shields.io/badge/dynamic/json.svg?label=release&url=https://pypi.org/pypi/cardano-method/json&query=%24.info.version&colorB=blue)](https://pypi.org/project/cardano-method/)

A fast, reliable Python library to solve cubic equations of all kinds. You can test out `cardano-method` [in your browser](https://replit.com/@Vndom/CardanoMethod-Playground#main.py).

## How It Works

`cardano-method` implements Gerolamo Cardano's famous method of solving cubic equations - 'Cardano's Method'. Split amongst various stages of processing, this library **mirrors the steps described in Cardano's Method**.

## Installation

```
$ pip install cardano-method
```

## Usage

```python
from cardano_method import CubicEquation

a = CubicEquation([1, 3, 4, 4])

print(a.answers)
# [(-2+0j), (-0.5+1.322875j), (-0.5-1.322875j)]
```

Note that the ``answers`` attribute contains a list of [`complex`](https://docs.python.org/3/library/cmath.html#module-cmath) objects representing the zeroes of the cubic equation.

<!-- ## How It Works

### How -->

<!-- definition of depressed cubic equation (mention that this is a specific case of the generalized idea of a depressed polynomial) -->

<!-- Cardano's Method is a multi-step process that allows the solutions of a cubic equation to be determined. -->

<!-- #### Depression of the Cubic Equation

$$p(x) = \sum_{i=0}^3 a_ix^i = a_3x^3 + a_2x_2 + a_1x_1 + a_0$$

$$p(x) = a(x-\alpha)(x-\beta)(x-\gamma)$$

Notice how $p\left(x-\frac{a_2}{3a_3}\right) = q(x)$! Substituting in  $q$ in terms of $p$ and its coefficients! Making the substitution and simplifying, we get

$$p(x) = a_3x^3 + a_2x^2 + a_1x + a_0$$

$$\Rightarrow p\left(x-\frac{a_2}{3a_3}\right) = q(x) = a_3x^3 + x\left(a_1-\frac{a_2^2}{3a_3}\right) + \left[\frac{2a_2^3}{27a_3^2} - \frac{a_1a_2}{3a_3} + a_0\right]$$

Then, after standardizing the coefficients to 1 and a bit more math and definitions, we arrive at the solutions to the given cubic equation:

$$\Bigg \{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}} - \frac{H}{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}} - \frac{a_2}{3a_3},  \sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}\omega - \frac{H\omega^2}{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}} - \frac{a_2}{3a_3}, \\ 
\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}\omega^2 - \frac{H\omega}{\sqrt[3]{\frac{-G + \sqrt{G^2+4H^3}}{2}}} - \frac{a_2}{3a_3}\Bigg \}$$

If this looks complicated, don't worry - we agree too! The CardanoMethod package's ``CubicEquation`` handles all of this on the back-end and abstracts away all of the complex math. -->