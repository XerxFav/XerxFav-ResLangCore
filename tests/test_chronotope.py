from arca_core.chronotope import Chronotope

def test_initial_state():
    c = Chronotope()
    assert c.state.name == "QND"
