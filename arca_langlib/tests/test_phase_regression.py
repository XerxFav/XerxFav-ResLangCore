from arca_core.phase import PhaseBit, QND_CONST
from arca_langlib.tests.test_phase_visualization import simulate_phase_transition

def test_regression_phase_logic():
    # Проверяем ключевые точки
    assert simulate_phase_transition(PhaseBit.QND, 0.99) == "Stable nondemolition regime"
    assert simulate_phase_transition(PhaseBit.QND, 1.01) == "Neutral regime"

    assert simulate_phase_transition(PhaseBit.PHASE, 0.99) == "Neutral regime"
    assert simulate_phase_transition(PhaseBit.PHASE, 1.00) == "Phase amplification regime"

    assert simulate_phase_transition(PhaseBit.ACT, 10.0) == "Neutral regime"
    assert simulate_phase_transition(PhaseBit.ACT, 10.01) == "High-energy active regime"
