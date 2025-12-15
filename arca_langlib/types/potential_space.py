# arca_langlib/types/potential_space.py
# Класс PotentialSpaceOperator — работа с глобальным и локальным потенциалом

import math

class PotentialSpaceOperator:
    """
    PotentialSpaceOperator — модуль для работы с глобальным и локальным потенциалом,
    временными объёмами и связкой массы-энергии.
    """

    def global_potential(self, Rglob: float, Vglob: float) -> float:
        return (4 * math.pi * Rglob**3) / Vglob

    def local_potential_obj(self, E: float) -> float:
        return (1 - E)**(2/3)

    def time_volume_global(self, psi0_obj: float, PsiGlob: float) -> float:
        return (1 + psi0_obj / PsiGlob)**(1/3)

    def time_volume_local(self, m0: float, v: float, C: float) -> float:
        return (1 / (m0 * (v/C)**2))**(1/3)
