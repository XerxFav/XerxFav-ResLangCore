# tests/arca_core_phase1/test_phase_types.py
from arca_core.phase1.phase_types import describe_phase

def test_describe_phase():
    assert "arca_core_phase1" in describe_phase()
