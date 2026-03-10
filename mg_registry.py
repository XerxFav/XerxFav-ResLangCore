"""
Automatic registry for Morphologic Geometry operators.
"""

import pkgutil
import inspect
import importlib

from .mg_operators import MorphologicOperators
from .mg_stability import MorphologicStability
from .mg_invariants import MorphologicInvariants


# ------------------------------------------------------------
# 1. ГЛАВНЫЙ РЕЕСТР
# ------------------------------------------------------------
registry = {}


# ------------------------------------------------------------
# 2. АВТОМАТИЧЕСКИЙ ПОИСК И ЗАГРУЗКА ОПЕРАТОРОВ
# ------------------------------------------------------------

def auto_register_operators():
    """
    Автоматически находит все классы в модулях morphology_engine,
    чьи имена заканчиваются на 'Operator' или 'Ternary' или 'Core'.
    """

    package = __package__  # arca_core.arca_morphology.morphology_engine

    for loader, module_name, is_pkg in pkgutil.iter_modules(__path__):
        # пропускаем системные файлы
        if module_name.startswith("mg_"):
            continue

        module = importlib.import_module(f"{package}.{module_name}")

        # ищем классы
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # оператор должен быть определён в этом модуле
            if obj.__module__ != module.__name__:
                continue

            # критерии оператора
            if (
                name.endswith("Operator")
                or name.endswith("Core")
                or name.endswith("Ternary")
            ):
                registry[module_name] = obj


# запускаем автозагрузку при импорте
auto_register_operators()


# ------------------------------------------------------------
# 3. ОБОЛОЧКА ДЛЯ ДВИЖКА
# ------------------------------------------------------------

class MorphologicRegistry:
    def __init__(self):
        self.ops = MorphologicOperators()
        self.stability = MorphologicStability()
        self.inv = MorphologicInvariants()

    def get(self, name):
        return registry.get(name)
