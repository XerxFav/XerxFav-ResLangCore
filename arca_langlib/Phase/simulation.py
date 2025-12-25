import math


def update_energy(E0: float, dE_t: float, dE_trigger: float) -> float:
    """
    Обновление энергии ячейки:
    E_new = E0 + dE_t + dE_trigger
    """
    return E0 + dE_t + dE_trigger


def update_volume(psi0: float, Psi_glob: float) -> float:
    """
    Перестройка фазового объёма:
    ΔV = ∛(1 + ψ0 / Ψ_glob)
    """
    return (1.0 + psi0 / Psi_glob) ** (1.0 / 3.0)


def stability_check(M: float, eps: float) -> bool:
    """
    Проверка устойчивости:
    stable = (M >= eps)
    """
    return M >= eps


def equilibrium_check(dpsi_dt: float, dE: float, eps: float) -> bool:
    """
    Проверка фазового равновесия:
    eq = (|dψ/dt| < eps) and (|dE| < eps)
    """
    return abs(dpsi_dt) < eps and abs(dE) < eps
