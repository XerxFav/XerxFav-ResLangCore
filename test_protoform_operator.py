# arca_langlib/tests/test_protoform_operator.py
import math
import pytest

from arca_langlib import ProtoFormOperator, Cluster, PotentialSpaceOperator, ResonanceOperator
from arca_core.protoform_operator
def test_invariant_phys():
    proto = ProtoFormOperator()
    result = proto.invariant_phys(V=10, V0=2, R=1)
    assert math.isclose(result, (10-2)/(4*math.pi*1**3))

def test_invariant_abs():
    proto = ProtoFormOperator()
    result = proto.invariant_abs(psi0=0.5, V=10, V0=2, R=1)
    assert isinstance(result, float)

def test_calc_n():
    proto = ProtoFormOperator()
    result = proto.calc_n(V=10, V0=2, R=1)
    assert math.isclose(result, (4*math.pi*1**3)/(10-2))

def test_resonance_operator_phase_shift():
    ro = ResonanceOperator()
    phase = ro.phase_shift(psi1=1.0, psi2=1.0)
    assert math.isclose(phase, math.atan2(1.0, 1.0))
# -------------------------------
# 🔹 ResonanceOperator — phase_shift
# -------------------------------

def test_phase_shift_quadrants():
    ro = ResonanceOperator()
    # Проверка разных квадрантов
    assert math.isclose(ro.phase_shift(1, 0), 0.0)          # угол 0
    assert math.isclose(ro.phase_shift(0, 1), math.pi/2)    # угол 90°
    assert math.isclose(ro.phase_shift(-1, 0), math.pi)     # угол 180°
    assert math.isclose(ro.phase_shift(0, -1), -math.pi/2)  # угол -90°
# -------------------------------
# 🔹 ResonanceOperator — coherence_check
# -------------------------------

def test_coherence_check_true_case():
    ro = ResonanceOperator()
    # x=y=z=1, n=2 → все r1,r2,r3 равны -1, допуск 1 → True
    assert ro.coherence_check(1, 1, 1, n=2, tol=1.0)

def test_coherence_check_false_case():
    ro = ResonanceOperator()
    # x=2,y=3,z=4,n=2 → большие разности, допуск маленький → False
    assert not ro.coherence_check(2, 3, 4, n=2, tol=0.1)

def test_coherence_check_with_zero_values():
    ro = ResonanceOperator()
    # x=0,y=0,z=0 → все r равны 0 → True даже при малом допуске
    assert ro.coherence_check(0, 0, 0, n=2, tol=0.01)

def test_coherence_check_negative_values():
    ro = ResonanceOperator()
    # отрицательные значения тоже должны корректно обрабатываться
    result = ro.coherence_check(-1, -1, -1, n=3, tol=5.0)
    assert isinstance(result, bool)


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
ef test_validity_even_mode(): op = ProtoFormOperator() # Для базовой реализации validity_signature(P) == P mode = op.classify_category(P1="a", P2="b", P3="a") assert mode == "even_category" def test_validity_odd_mode(): op = ProtoFormOperator() mode = op.classify_category(P1="a", P2="b", P3="c") assert mode == "odd_category" def test_resonance_volume_basic(): op = ProtoFormOperator() result = op.resonance_volume(P1="a", P2="b", P3="a", V=2.0, V0=1.0, R=1.0) assert result["mode"] == "even_category" assert math.isclose(result["volume"], (2.0 - 1.0) / (4 * math.pi * 1.0**3)) assert result["signature"]["P1"] == "a" assert result["signature"]["P2"] == "b" assert result["signature"]["P3"] == "a" def test_iterate_configuration_even_then_odd(): op = ProtoFormOperator() C0 = {"params": []} C1, mode1 = op.iterate_configuration(C0, "a") assert C1["params"] == ["a"] assert C1["last_mode"] == "odd_category" assert mode1 == "odd_category" C2, mode2 = op.iterate_configuration(C1, "b") assert C2["params"] == ["a", "b"] assert C2["last_mode"] == "odd_category" assert mode2 == "odd_category" C3, mode3 = op.iterate_configuration(C2, "a") assert C3["params"] == ["a", "b", "a"] assert C3["last_mode"] == "even_category" assert mode3 == "even_category" 
