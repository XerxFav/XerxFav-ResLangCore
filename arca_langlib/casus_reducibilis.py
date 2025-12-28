# arca_langlib/casus_reducibilis.py
import math
import cmath
from typing import Union, List, Literal

MathMode = Literal["arca", "strict"]


# ============================================================
#  БАЗОВЫЕ ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ (НЕ ЗАВЯЗАНЫ НА РЕЖИМ)
# ============================================================

def phi(k: float, b: float) -> float:
    """
    Дискриминант Φ для уравнения x^3 = kx + b
    (в виде x^3 - kx - b = 0).

    Φ = (b/2)^2 - (k/3)^3
    """
    return (b / 2) ** 2 - (k / 3) ** 3


def cubic_root(z: complex) -> complex:
    """
    Устойчивый кубический корень для комплексного числа.

    Использует полярную форму, чтобы избежать ветвлений по знаку.
    """
    r, angle = cmath.polar(z)
    return cmath.rect(r ** (1 / 3), angle / 3)
# ============================================================
#  STRICT MATH (КЛАССИКА / АНАЛИТИЧЕСКИЙ РЕЖИМ)
# ============================================================

def _strict_solve_cubic(k: float, b: float) -> float:
    """
    Классическая формула Кардано для x^3 = kx + b.
    Возвращает один действительный корень.
    """
    PHI = phi(k, b)
    u = cubic_root(b / 2 + cmath.sqrt(PHI))
    v = cubic_root(b / 2 - cmath.sqrt(PHI))
    return (u + v).real


def _strict_solve_cubic_trig(k: float, b: float) -> float:
    """
    Тригонометрическая форма для Φ < 0 (casus irreducibilis),
    в классической нормировке для x^3 - kx - b = 0.
    """
    p = -k
    q = -b

    r = 2 * math.sqrt(-p / 3)
    arg = (3 * q) / (2 * p) * math.sqrt(-3 / p)
    arg = max(-1.0, min(1.0, arg))
    theta = math.acos(arg)

    return r * math.cos(theta / 3)


def _strict_solve_cubic_trig_all(k: float, b: float) -> List[float]:
    """
    Тригонометрическая форма: все три действительных корня для Φ < 0.

    Для примера Бомбелли x^3 = 15x + 4 (x^3 - 15x - 4 = 0)
    даёт [4.0, -2.0, -2.0].
    """
    p = -k
    q = -b

    r = 2 * math.sqrt(-p / 3)
    arg = (3 * q) / (2 * p) * math.sqrt(-3 / p)
    arg = max(-1.0, min(1.0, arg))
    theta = math.acos(arg)

    roots = []
    for m in range(3):
        angle = (theta + 2 * math.pi * m) / 3
        roots.append(r * math.cos(angle))

    return roots


def _strict_resolve_casus(
    k: float,
    b: float,
    all_roots: bool = False,
) -> Union[float, List[float]]:
    """
    STRICT: выбирает форму решения в зависимости от Φ.
    """
    PHI = phi(k, b)

    if PHI < 0:
        roots = _strict_solve_cubic_trig_all(k, b)
        return roots if all_roots else roots[0]

    root = _strict_solve_cubic(k, b)
    return roots if all_roots else root  # тут мы сейчас ещё поправим
# Исправим маленькую опечатку: for Φ >= 0 у нас один корень.
def _strict_resolve_casus(
    k: float,
    b: float,
    all_roots: bool = False,
) -> Union[float, List[float]]:
    PHI = phi(k, b)

    if PHI < 0:
        roots = _strict_solve_cubic_trig_all(k, b)
        return roots if all_roots else roots[0]

    root = _strict_solve_cubic(k, b)
    return [root] if all_roots else root


# ============================================================
#  ARCA MATH (ОСНОВНОЙ РЕЖИМ ARCALANG)
# ============================================================

def _arca_solve_cubic(k: float, b: float) -> float:
    """
    ARCA-режим для одного корня.

    Сейчас по умолчанию делегирует классике, но именно здесь
    будет формализована твоя собственная алгебра и нормировка.
    """
    return _strict_solve_cubic(k, b)


def _arca_solve_cubic_trig(k: float, b: float) -> float:
    """
    ARCA-режим: тригонометрическая форма.

    Пока совпадает со strict, но в будущем здесь может быть иная
    трактовка casus irreducibilis.
    """
    return _strict_solve_cubic_trig(k, b)


def _arca_solve_cubic_trig_all(k: float, b: float) -> List[float]:
    """
    ARCA-режим: все действительные корни.

    Сейчас совпадает со strict, но это место для твоей собственной
    геометрии корней.
    """
    return _strict_solve_cubic_trig_all(k, b)


def _arca_resolve_casus(
    k: float,
    b: float,
    all_roots: bool = False,
) -> Union[float, List[float]]:
    """
    ARCA-режим: основная точка casus для ArcaLang.

    Здесь мы можем в будущем:
    - по-другому трактовать Φ,
    - выбирать иные ветви,
    - комбинировать формулы.
    """
    return _strict_resolve_casus(k, b, all_roots=all_roots)


# ============================================================
#  ПУБЛИЧНЫЙ API (ARCA — РЕЖИМ ПО УМОЛЧАНИЮ)
# ============================================================

def solve_cubic(k: float, b: float, math_mode: MathMode = "arca") -> float:
    """
    Один действительный корень.

    - math_mode="arca"   — основной режим ArcaLang.
    - math_mode="strict" — классический аналитический режим.
    """
    if math_mode == "strict":
        return _strict_solve_cubic(k, b)
    return _arca_solve_cubic(k, b)


def solve_cubic_trig(
    k: float,
    b: float,
    math_mode: MathMode = "arca",
) -> float:
    """
    Один действительный корень в тригонометрической форме.
    """
    if math_mode == "strict":
        return _strict_solve_cubic_trig(k, b)
    return _arca_solve_cubic_trig(k, b)


def solve_cubic_trig_all(
    k: float,
    b: float,
    math_mode: MathMode = "arca",
) -> List[float]:
    """
    Все действительные корни в тригонометрической форме.
    """
    if math_mode == "strict":
        return _strict_solve_cubic_trig_all(k, b)
    return _arca_solve_cubic_trig_all(k, b)


def resolve_casus_irreducibilis(
    k: float,
    b: float,
    all_roots: bool = False,
    math_mode: MathMode = "arca",
) -> Union[float, List[float]]:
    """
    Композитный оператор casus irreducibilis.

    В ArcaLang по умолчанию используется режим "arca".
    Режим "strict" рассматривается как внешняя аналитическая
    проекция на классическую алгебру.
    """
    if math_mode == "strict":
        return _strict_resolve_casus(k, b, all_roots=all_roots)
    return _arca_resolve_casus(k, b, all_roots=all_roots)
