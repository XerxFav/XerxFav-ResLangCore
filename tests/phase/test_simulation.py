import math
from arca_langlib.Phase import simulation


def test_update_energy():
    E = simulation.update_energy(E0=1.0, dE_t=0.5, dE_trigger=0.5)
    assert math.isclose(E, 2.0, rel_tol=1e-9)


def test_update_volume():
    V = simulation.update_volume(psi0=1.0, Psi_glob=1.0)
    assert math.isclose(V, 2 ** (1/3), rel_tol=1e-9)


def test_stability_check_true():
    assert simulation.stability_check(M=0.7, eps=0.6) is True


def test_stability_check_false():
    assert simulation.stability_check(M=0.5, eps=0.6) is False
