from arca_core.chronotope import Chronotope
from arca_core.phase import Phase

def test_initial_state():
    c = Chronotope()
    assert c.state.name == "QND"

def test_phase_transition():
    p = Phase("neutral")
    assert p.transition("positive") == "positive"
