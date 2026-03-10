"""
Morphologic Geometry — Fundamental Operators
I(x), S(x), T(R,r), U(...)
"""

import math


class MorphologicOperators:
    """
    Набор морфологических операторов:
    - I(x): радикальная симметрия
    - S(x): радиальная рекурсия
    - T(R,r): рекурсивная тороидальная инвариантность
    - U(...): оператор устойчивой геометрии
    """

    

    def I(self, x: float) -> float:
        return x

    def S(self, x: float) -> float:
        return x

    def T(self, R: float, r: float) -> float:
        # Canon: мягкая тороидальная рекурсия
        return (R + r) / 2.0

    def U(self, R: float, r: float) -> float:
        # Canon: мягкая устойчивая геометрия
        return (R + r) / 2.0
