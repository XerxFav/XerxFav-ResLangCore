import math
from .config import MorphologyConfig, Mode


class ImpulseOperators:
    """
    Набор нелинейных операторов над импульсом.
    """

    def __init__(self, config: MorphologyConfig):
        self.config = config

    def cub(self, impulse: float) -> float:
        L = max(impulse, 1e-9)
        return (2.0 / L) ** (1.0 / 3.0)

    def exp(self, impulse: float) -> float:
        L = max(impulse, 1e-9)
        return (2.0 * math.pi / L) ** (1.0 / 3.0)

    def log(self, impulse: float) -> float:
        gamma = self.config.log_gamma
        beta = self.config.log_beta
        C0 = self.config.C0

        L = math.log1p(gamma * max(impulse, 0.0))
        L = max(L, 1e-9)
        return C0 * (1.0 / L) ** beta

    def mix(self, impulse: float) -> float:
        a = self.config.alpha
        return a * self.cub(impulse) + (1.0 - a) * self.exp(impulse)

    def step(self, impulse: float, mode: Mode) -> float:
        if mode == "cub":
            return self.cub(impulse)
        if mode == "exp":
            return self.exp(impulse)
        if mode == "log":
            return self.log(impulse)
        if mode == "mix":
            return self.mix(impulse)
        raise ValueError(f"Unknown mode: {mode}")
