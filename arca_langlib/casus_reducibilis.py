# arca_langlib/casus_reducibilis.py
import math
import cmath
from typing import Optional, Tuple, Union, List

def phi(k: float, b: float) -> float:
    """Вычисляет дискриминант Φ для кубического уравнения x^3 = kx + b."""
    return (b/2)**2 - (k/3)**3

def cubic_root(z: complex) -> complex:
    """Устойчивый кубический корень для комплексного числа."""
    r, angle = cmath.polar(z)
    return cmath.rect(r**(1/3), angle/3)

def solve_cubic(k: float, b: float) -> float:
    """Комплексная форма Кардано: возвращает один действительный корень."""
    PHI = phi(k, b)
    u = cubic_root(b/2 + cmath.sqrt(PHI))
    v = cubic_root(b/2 - cmath.sqrt(PHI))
    return (u + v).real

def solve_cubic_trig(k: float, b: float) -> float:
    """Тригонометрическая форма для Φ < 0: устойчивый реальный корень."""
    p = -k
    q = -b
    if p >= 0:
        return solve_cubic(k, b)
    r = 2 * math.sqrt(-p/3)
    arg = (q/2) / math.sqrt(- (p/3)**3)
    arg = max(-1.0, min(1.0, arg))
    theta = math.acos(arg)
    return r * math.cos(theta/3)

def solve_cubic_trig_all(k: float, b: float) -> List[float]:
    """Тригонометрическая форма для Φ < 0: возвращает все три действительных корня."""
    p = -k
    q = -b
    if p >= 0:
        return [solve_cubic(k, b)]
    r = 2 * math.sqrt(-p/3)
    arg = (q/2) / math.sqrt(- (p/3)**3)
    arg = max(-1.0, min(1.0, arg))
    theta = math.acos(arg)
    roots = []
    for m in range(3):
        angle = (theta + 2*math.pi*m) / 3
        roots.append(r * math.cos(angle))
    return roots

def pick_conjugate_pair(k: float, b: float, search_radius: int = 10, step: float = 1.0) -> Optional[Tuple[float, float]]:
    """Эвристический выбор (a,b) для u=a+bi, v=a-bi."""
    target_uv = k / 3
    target_real = b / 2
    a_range = [i*step for i in range(-search_radius, search_radius+1)]
    b_range = [j*step for j in range(-search_radius, search_radius+1)]
    for a in a_range:
        for bb in b_range:
            if abs(a**2 + bb**2 - target_uv) < 1e-9:
                if abs(a**3 - 3*a*(bb**2) - target_real) < 1e-9:
                    return a, bb
    return None

def resolve_casus_irreducibilis(k: float, b: float, all_roots: bool = False) -> Union[float, List[float]]:
    """
    Композитный оператор: эвристика → тригонометрия → Кардано.
    - Если Φ < 0: casus irreducibilis → эвристика или тригонометрическая форма.
    - Если Φ ≥ 0: стандартная формула Кардано.
    """
    PHI = phi(k, b)
    if PHI < 0:
        pair = pick_conjugate_pair(k, b)
        if pair is not None and not all_roots:
            a, _b = pair
            return float(2*a)
        roots = solve_cubic_trig_all(k, b)
        return roots if all_roots else roots[0]
    return solve_cubic(k, b)
