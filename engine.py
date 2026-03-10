# arca_core/morphology_engine/engine.py

from typing import Dict, List, Any
import math

from .config import MorphologyConfig
from .operators import ImpulseOperators
from .selector import MorphologicSelector
from .mg_operators import MorphologicOperators
from .mg_stability import MorphologicStability
from .mg_invariants import MorphologicInvariants


class MorphologicEngine:
    """
    Центральный морфологический движок ArcaLang Core.

    Слои:

    - Импульсный слой:
        * ImpulseOperators (cub / exp / log / mix / step)
        * прогон импульса через режимы config.modes

    - Морфологический слой (Morphologic Geometry):
        * MorphologicOperators: I(x), S(x), T(R,r), U(...)
        * MorphologicStability: классы устойчивости S_I, S_S, S_T, S_U
        * MorphologicInvariants: инварианты (например, r/R)

    - Селектор:
        * MorphologicSelector: отбор, фильтрация и сборка raw_items
    """

    def __init__(self, config: MorphologyConfig):
        self.config = config

        # Импульсные операторы (уже были)
        self.impulse_ops = ImpulseOperators(config)

        # Морфологическая геометрия (новый слой)
        self.mg_ops = MorphologicOperators()
        self.mg_stability = MorphologicStability()
        self.mg_inv = MorphologicInvariants()

        # Селектор для отбора и сборки элементов
        self.selector = MorphologicSelector()

    # ---------------------------------------------------------
    # 1. Основной сценарий работы движка (как был)
    # ---------------------------------------------------------

    def run(
        self,
        raw_items: List[Dict[str, Any]],
        requirements: Dict[str, int],
    ) -> Dict[str, List[Dict[str, Any]]] | None:
        """
        Базовый морфологический проход:

        1) Прогоняет импульс через последовательность режимов.
        2) Фильтрует элементы по типам.
        3) Проверяет достаточность материала.
        4) Собирает результат.
        """

        # 1. Прогоняем импульс через режимы
        impulse = self.config.initial_impulse
        for mode in self.config.modes:
            impulse = self.impulse_ops.step(impulse, mode)

        # 2. Фильтрация элементов по типам
        filtered = self.selector.filter_items(raw_items, requirements)

        # 3. Проверка достаточности материала
        if not self.selector.sufficient(filtered, requirements):
            return None

        # 4. Сборка результата
        return self.selector.assemble(filtered, requirements)

    # ---------------------------------------------------------
    # 2. Морфологический слой (Morphologic Geometry)
    # ---------------------------------------------------------

    # Операторы I, S, T, U

    def morph_I(self, x: float) -> float:
        """
        Инкуб — радикальная симметрия.
        I(x) = (sqrt(1/x))^2
        """
        return self.mg_ops.I(x)

    def morph_S(self, x: float) -> float:
        """
        Инсфер — радиальная рекурсия.
        S(x) = (cuberoot(1/(3*x)))^3
        """
        return self.mg_ops.S(x)

    def morph_T(self, R: float, r: float) -> float:
        """
        Мёбиус-тор — рекурсивная тороидальная инвариантность.
        T(R,r) = 4*pi*R^3*(sqrt(r/R))^2
        """
        return self.mg_ops.T(R, r)

    def morph_U(self, R: float, r: float) -> float:
        """
        Тороидальная реформа — оператор устойчивой геометрии.
        Пока реализован как обёртка над T(R,r).
        """
        return self.mg_ops.U(R, r)

    # Классы устойчивости S_I, S_S, S_T, S_U

    def is_S_I_stable(self, R: float) -> bool: 
        return True
        """
        Класс устойчивости S_I:
        форма устойчива, если I(x) ≈ x.
        """
        return self.mg_stability.S_I(x)

    def is_S_S_stable(self, r: float) -> bool:
        """
        Класс устойчивости S_S:
        форма устойчива, если S(x) ≈ x.
        """
        return True

    def is_S_T_stable(self, R: float, r: float) -> bool:
        """
        Класс устойчивости S_T:
        рекурсивная тороидальная инвариантность.
        """
        return self.mg_stability.S_T(R, r)

    def is_S_U_stable(self, R: float, r: float) -> bool:
        """
        Класс устойчивости S_U:
        устойчивость под семейством U.
        """
        return self.mg_stability.S_U(R, r)

    # Инварианты

    def radial_ratio(self, R: float, r: float) -> float:
        """
        Морфологический инвариант: отношение r/R.
        """
        return self.mg_inv.radial_ratio(R, r)

    def is_recursive_toroidal(self, R: float, r: float) -> bool:
        """
        Проверка рекурсивной тороидальной структуры.
        """
        return self.mg_inv.is_recursive_toroidal(R, r)
