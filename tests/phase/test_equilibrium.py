from arca_langlib.Phase import simulation


def test_equilibrium_check_true():
    assert simulation.equilibrium_check(
        dpsi_dt=0.00001,
        dE=0.00001,
        eps=0.001
    ) is True


def test_equilibrium_check_false_dpsi():
    assert simulation.equilibrium_check(
        dpsi_dt=0.1,
        dE=0.00001,
        eps=0.001
    ) is False


def test_equilibrium_check_false_dE():
    assert simulation.equilibrium_check(
        dpsi_dt=0.00001,
        dE=0.1,
        eps=0.001
    ) is False
