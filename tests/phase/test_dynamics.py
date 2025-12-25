import math
from arca_langlib.Phase import dynamics


def test_energy_trigger_center():
    dE = dynamics.energy_trigger(A=1.0, dx=0, dy=0, dz=0, sigma=1.0)
    assert math.isclose(dE, 1.0, rel_tol=1e-9)


def test_energy_trigger_offset():
    dE = dynamics.energy_trigger(A=1.0, dx=1, dy=0, dz=0, sigma=1.0)
    assert dE < 1.0


def test_memory_adapt():
    psi_new = dynamics.memory_adapt(psi0=1.0, E=2.0, Ecrit=1.0)
    assert math.isclose(psi_new, 1.0 * (1 - (2 - 1)/2), rel_tol=1e-9)


def test_correlation_equal():
    M = dynamics.correlation(psi_i=1.0, psi_j=1.0, Psi_glob=1.0)
    assert math.isclose(M, 1.0, rel_tol=1e-9)


def test_correlation_different():
    M = dynamics.correlation(psi_i=1.0, psi_j=2.0, Psi_glob=1.0)
    assert M < 1.0


def test_resonance_condition():
    R = dynamics.resonance_condition(Psi=4.0, psi0=1.0, E=2.0)
    assert math.isclose(R, 4.0 - 4.0, rel_tol=1e-9)
