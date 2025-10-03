def test_phase_generation():
    from arca_fieldcore.generator import generate_phase
    assert generate_phase("neutral") in ["positive", "negative"]
