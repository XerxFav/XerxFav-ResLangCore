import pytest
from arca_core.phase import Phase

@pytest.mark.phase
@pytest.mark.parametrize("initial,transition,target", [
    ("neutral", "positive", "positive"),
    ("positive", "negative", "negative"),
    ("negative", "neutral", "neutral"),
])
def test_phase_transition(initial, transition, target):
    p = Phase(initial)
    result = p.transition(transition)
    assert result == target
