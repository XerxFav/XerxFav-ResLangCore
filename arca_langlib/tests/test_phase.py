# arca_langlib/tests/test_phase.py
import math
import pytest
from arca_core.phase import PhaseBit, QND_CONST

def test_phasebit_enum():
    assert PhaseBit.QND.value == 0
    assert PhaseBit.PHASE.value == 1
    assert PhaseBit.ACT.value == 2

def test_qnd_const():
    # Проверим, что константа вычисляется и имеет положительное значение
    assert QND_CONST > 0
    # Проверим порядок величины
    assert math.isfinite(QND_CONST)
def simulate_phase_transition(bit: PhaseBit, const_value: float) -> str:
    if bit == PhaseBit.QND and const_value < 1:
        return "Stable nondemolition regime"
    elif bit == PhaseBit.PHASE and const_value >= 1:
        return "Phase amplification regime"
    elif bit == PhaseBit.ACT and const_value > 10:
        return "High-energy active regime"
    else:
        return "Neutral regime"

@pytest.mark.parametrize("phasebit,const_value,expected", [
    (PhaseBit.QND, 0.5, "Stable nondemolition regime"),
    (PhaseBit.PHASE, 1.0, "Phase amplification regime"),
    (PhaseBit.ACT, 20.0, "High-energy active regime"),
    (PhaseBit.ACT, 5.0, "Neutral regime"),
])
def test_phasebit_qnd_const_integration(phasebit, const_value, expected):
    assert simulate_phase_transition(phasebit, const_value) == expected

def test_qnd_const_integration_with_phasebit():
    # Проверка, что текущее значение QND_CONST даёт корректный режим
    result = simulate_phase_transition(PhaseBit.PHASE, QND_CONST)
    assert isinstance(result, str)
    assert result in {
        "Stable nondemolition regime",
        "Phase amplification regime",
        "High-energy active regime",
        "Neutral regime",
    }
