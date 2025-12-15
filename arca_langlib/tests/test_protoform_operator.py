# arca_langlib/tests/test_protoform_operator.py
import math
import pytest

from arca_langlib import ProtoFormOperator, Cluster, PotentialSpaceOperator, ResonanceOperator

def test_invariant_phys():
    proto = ProtoFormOperator()
    result = proto.invariant_phys(V=10, V0=2, R=1)
    assert math.isclose(result, (10-2)/(4*math.pi*1**3))



def test_invariant_abs():
    proto = ProtoFormOperator()
    result = proto.invariant_abs(psi0=0.5, V=10, V0=2, R=1)
    assert isinstance(result, float)

# -------------------------------
# 🔹 Параметризованные тесты
# -------------------------------

@pytest.mark.parametrize(
    "V,V0,R,expected",
    [
        (10, 2, 1, (10-2)/(4*math.pi*1**3)),
        (20, 5, 2, (20-5)/(4*math.pi*2**3)),
        (15, 3, 0.5, (15-3)/(4*math.pi*0.5**3)),
    ]
)
def test_invariant_phys_param(V, V0, R, expected):
    proto = ProtoFormOperator()
    result = proto.invariant_phys(V=V, V0=V0, R=R)
    assert math.isclose(result, expected)


@pytest.mark.parametrize(
    "psi0,V,V0,R",
    [
        (0.1, 10, 2, 1),
        (0.5, 20, 5, 2),
        (0.9, 15, 3, 0.5),
    ]
)
def test_invariant_abs_param(psi0, V, V0, R):
    proto = ProtoFormOperator()
    result = proto.invariant_abs(psi0=psi0, V=V, V0=V0, R=R)
    assert isinstance(result, float)


@pytest.mark.parametrize(
    "x,y,z,n",
    [
        (1, 1, 1, 2),
        (2, 3, 4, 3),
        (0.5, 0.5, 0.5, 4),
    ]
)
def test_psi1_and_psi2(x, y, z, n):
    proto = ProtoFormOperator()
    psi1 = proto.psi1(x, y, z, n)
    psi2 = proto.psi2(x, y, z, n)
    assert isinstance(psi1, (int, float))
    assert isinstance(psi2, (int, float))



def test_calc_n():
    proto = ProtoFormOperator()
    result = proto.calc_n(V=10, V0=2, R=1)
    assert math.isclose(result, (4*math.pi*1**3)/(10-2))

def test_resonance_operator_phase_shift():
    ro = ResonanceOperator()
    phase = ro.phase_shift(psi1=1.0, psi2=1.0)
    assert math.isclose(phase, math.atan2(1.0, 1.0))

def test_cluster_add_and_size():
    proto = ProtoFormOperator()
    cluster = Cluster()
    cluster.add(proto)
    assert cluster.size() == 1

def test_potential_space_global_local():
    ps = PotentialSpaceOperator()
    glob = ps.global_potential(Rglob=1.0, Vglob=2.0)
    assert math.isclose(glob, (4*math.pi*1.0**3)/2.0)

    local = ps.local_potential_obj(E=0.5)
    assert isinstance(local, float)

def test_mass_energy_link():
    proto = ProtoFormOperator()
    ok = proto.mass_energy_link(E=4, R0=1, m0=1, v=1, C=1, psi0_obj=1)
    assert isinstance(ok, bool)
