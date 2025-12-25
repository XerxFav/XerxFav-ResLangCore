import math
from arca_langlib.Phase import geometry


def test_sphere_volume():
    assert math.isclose(
        geometry.sphere_volume(1.0),
        4/3 * math.pi,
        rel_tol=1e-9
    )


def test_torus_volume():
    assert math.isclose(
        geometry.torus_volume(1.0, 0.5),
        2 * math.pi**2 * 1.0 * 0.5**2,
        rel_tol=1e-9
    )


def test_global_volume_from_Psiobj():
    val = geometry.global_volume_from_Psiobj(2.0)
    assert math.isclose(val, (1 / (2.0**2)) ** (1/3), rel_tol=1e-9)


def test_geom_density():
    val = geometry.geom_density(1.0, 4 * math.pi)
    assert math.isclose(val, 1.0, rel_tol=1e-9)
