# arca_langlib/types/resonance_operator.py
# Класс ResonanceOperator — работа с фазовыми состояниями

import math

class ResonanceOperator:
    """
    ResonanceOperator — оператор для анализа резонансных состояний:
    фазовый сдвиг, проверка когерентности, усиление.
    """

    def phase_shift(self, psi1: float, psi2: float) -> float:
        return math.atan2(psi2, psi1)

    def coherence_check(self, x: float, y: float, z: float, n: int, tol: float = 1e-9) -> bool:
        S = x**n + y**n + z**n
        r1 = x**n - (y**n + z**n)
        r2 = y**n - (x**n + z**n)
        r3 = z**n - (x**n + y**n)
        return abs(r1) <= tol and abs(r2) <= tol and abs(r3) <= tol

    def amplify(self, psi2: float, gain: float) -> float:
        return psi2 * gain
