import pytest
import matplotlib.pyplot as plt
from arca_core.phase import PhaseBit, QND_CONST

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
    (PhaseBit.QND, 2.0, "Neutral regime"),
    (PhaseBit.PHASE, 0.5, "Neutral regime"),
    (PhaseBit.PHASE, 1.0, "Phase amplification regime"),
    (PhaseBit.ACT, 5.0, "Neutral regime"),
    (PhaseBit.ACT, 20.0, "High-energy active regime"),
])
def test_phasebit_thresholds(phasebit, const_value, expected):
    assert simulate_phase_transition(phasebit, const_value) == expected

def test_generate_phase_transition_plot(tmp_path):
    values = list(range(0, 21))
    fig, ax = plt.subplots()

    for bit, color in [
        (PhaseBit.QND, "blue"),
        (PhaseBit.PHASE, "green"),
        (PhaseBit.ACT, "red")
    ]:
        regimes = [simulate_phase_transition(bit, v) for v in values]
        ax.plot(values, regimes, label=bit.name, color=color)

    ax.set_xlabel("QND_CONST value")
    ax.set_ylabel("Regime")
    ax.legend()
    fig.tight_layout()

    output_file = tmp_path / "phase_transition_plot.png"
    fig.savefig(output_file)

    assert output_file.exists()
