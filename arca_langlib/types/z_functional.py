# ArcaLang/arca_langlib/types/z_functional.py
import numpy as np
from typing import Callable

class ZFunctional:
    """
    Оператор Z: интегральная суперпозиция с ядром памяти k(S) и энергетическим слоем V(Z).
    """

    def __init__(
        self,
        kernel: Callable[[np.ndarray], np.ndarray] = lambda s: np.exp(-0.1 * s),
        R: float = 1.0,
        m: float = 1.0,
        c: float = 3.0e8,
        V0: float = 0.0,
    ):
        self.kernel = kernel
        self.R = R
        self.m = m
        self.c = c
        self.V0 = V0

    def compute_Z(self, t: np.ndarray, x: np.ndarray, dt: float) -> float:
        """
        Дискретный функционал Z = ∫ k(S) x(S) dS, ориентированный на будущее окно.
        """
        if t.shape != x.shape:
            raise ValueError("t и x должны иметь одинаковую форму.")
        return float(np.sum(self.kernel(t) * x) * dt)

    def energy(self, Z: float) -> float:
        """
        Энергия E(Z): базовое сопоставление (можно заменить на нелинейное).
        """
        return Z

    def potential(self, Z: float) -> float:
        """
        Эффективный потенциал V(Z) = V0 + 4π R^3 · E(Z)/(m c^2).
        """
        E = self.energy(Z)
        return float(self.V0 + 4.0 * np.pi * (self.R ** 3) * (E / (self.m * self.c ** 2)))
