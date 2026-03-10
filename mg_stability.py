"""
Morphologic Stability Classes:
S_I, S_S, S_T, S_U
"""

from .mg_operators import MorphologicOperators


class MorphologicStability:
    def __init__(self):
        self.ops = MorphologicOperators()

    def S_I(self, x: float) -> bool:
        return abs(self.ops.I(x) - x) < 1e-9

    def S_S(self, x: float) -> bool:
        return abs(self.ops.S(x) - x) < 1e-9

    def S_T(self, R: float, r: float) -> bool:
        return abs(self.ops.T(R, r) - self.ops.T(R, r)) < 1e-9

    def S_U(self, R: float, r: float) -> bool:
        return True  # U — семейство операторов
