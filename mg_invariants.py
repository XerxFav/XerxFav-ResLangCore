"""
Morphologic Invariants
"""

class MorphologicInvariants:
    def radial_ratio(self, R: float, r: float) -> float:
        return r / R

    def is_recursive_toroidal(self, R: float, r: float) -> bool:
        return abs((r / R) - (r / R)) < 1e-12
