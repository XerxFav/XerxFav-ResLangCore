import math
from arca_langlib.Phase import core


def test_psi0_from_E_zero():
    assert math.isclose(core.psi0_from_E(0.0), 1.0, rel_tol=1e-9)


def test_psi0_from_E_one():
    assert math.isclose(core.psi0_from_E(1.0), 0.0, rel_tol=1e-9)


def test_psiglob_basic():
    val = core.psiglob_from_R_V(1.0, 2.0, 1.0)
    assert math.isclose(val, 4 * math.pi, rel_tol=1e-9)


def test_deltaV():
    val = core.deltaV_from_psi0_Psiglob(1.0, 1.0)
    assert math.isclose(val, 2 ** (1/3), rel_tol=1e-9)


def test_phase_density():
    val = core.phase_density(2.0, 1.0, 1.0)
    assert math.isclose(val, 1 / (4 * math.pi), rel_tol=1e-9)


def test_energy_density():
    val = core.energy_density(2.0, 1.0)
    assert math.isclose(val, 2 / (4 * math.pi), rel_tol=1e-9)


def test_m_effective():
    m0 = core.m_effective_from_E_R0_psi0(E=1.0, R0=1.0, psi0=1.0, v_over_c=0.5)
    expected = 1.0 / (4 * math.pi * (0.5 ** 2))
    assert math.isclose(m0, expected, rel_tol=1e-9)


def test_resonance_ratio():
    assert core.resonance_ratio(10.0, 2.0) == 5.0


def test_phase_index_n():
    val = core.phase_index_n(1.0, 2.0, 1.0)
    assert math.isclose(val, 4 * math.pi, rel_tol=1e-9)
