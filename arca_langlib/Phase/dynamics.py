import math


def energy_trigger(A: float, dx: float, dy: float, dz: float, sigma: float) -> float:
    r2 = dx * dx + dy * dy + dz * dz
    return A * math.exp(-r2 / (sigma ** 2))


def memory_adapt(psi0: float, E: float, Ecrit: float) -> float:
    return psi0 * (1.0 - (E - Ecrit) / E)


def correlation(psi_i: float, psi_j: float, Psi_glob: float) -> float:
    return math.exp(-abs(psi_i - psi_j) / Psi_glob)


def resonance_condition(Psi: float, psi0: float, E: float) -> float:
    return Psi / psi0 - (E ** 2)
