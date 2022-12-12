import pytest

from numpy.testing import assert_allclose

from preliz import quartile
from preliz.distributions import (
    Beta,
    Cauchy,
    ChiSquared,
    Exponential,
    Gamma,
    Gumbel,
    HalfCauchy,
    HalfNormal,
    HalfStudent,
    InverseGamma,
    Laplace,
    Logistic,
    LogNormal,
    Moyal,
    Normal,
    Pareto,
    Student,
    TruncatedNormal,
    Uniform,
    VonMises,
    Wald,
    Weibull,
    # DiscreteUniform,
    NegativeBinomial,
    Poisson,
)


@pytest.mark.parametrize(
    "distribution, q1, q2, q3, result",
    [
        (Beta, 0.3, 0.5, 0.7, (1.528, 1.528)),
        (Cauchy, -1, 0, 1, (0, 1)),
        (ChiSquared, 2, 4, 5.5, (4.329)),
        (Exponential, 0.5, 1, 2.5, (0.611)),
        (Gamma, 0.5, 1, 2.5, (0.894, 0.523)),
        (Gumbel, 0.5, 1, 2.5, (0.751, 1.265)),
        (HalfCauchy, 0.5, 1, 3, (1.105)),
        (HalfNormal, 0.5, 1, 2, (1.613)),
        (HalfStudent, 0.5, 1, 2, (1.366)),
        (InverseGamma, 0.2, 0.3, 0.4, (3.881, 1.019)),
        (Laplace, -1, 0, 1, (0, 1.442)),
        (Logistic, -1, 0, 1, (0, 0.910)),
        (LogNormal, 0.5, 1, 2, (0, 1.027)),
        (Moyal, 0.5, 1, 2, (0.620, 0.567)),
        (Normal, -1, 0, 1, (0, 1.482)),
        (Pareto, 0.5, 1, 4, (0.541, 0.289)),
        (Student, -1, 0, 1, (0, 1.307)),
        (TruncatedNormal, -1, 0, 1, (0, 1.482)),
        (Uniform, -1, 0, 1, (-2, 2)),
        (VonMises, -1, 0, 1, (0, 0.656)),
        (Wald, 0.5, 1, 2, (1.698, 1.109)),
        (Weibull, 0.5, 1, 2, (1.109, 1.456)),
        # (DiscreteUniform, -1, 0, 1, (-5, 5)), # the mass is 0.27 instead of 0.5
        (NegativeBinomial, 3, 5, 10, (7.283, 2.167)),
        (Poisson, 4, 5, 6, (5.641)),
    ],
)
def test_quartile(distribution, q1, q2, q3, result):
    _, opt = quartile(distribution(), q1, q2, q3)

    assert_allclose(opt.x, result, atol=0.001)