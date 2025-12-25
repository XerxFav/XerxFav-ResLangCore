import numpy as np


def inner_product(f, g, a: float, b: float, n: int = 2000) -> float:
    """
    Скалярное произведение в L2[a,b]:
    <f, g> = ∫ f(x) g(x) dx
    """
    x = np.linspace(a, b, n)
    return np.trapz(f(x) * g(x), x)


def norm(f, a: float, b: float, n: int = 2000) -> float:
    """
    Норма функции:
    ||f|| = sqrt(<f, f>)
    """
    return np.sqrt(inner_product(f, f, a, b, n))


def projection(f, g, a: float, b: float, n: int = 2000):
    """
    Ортогональная проекция f на g:
    proj_g(f) = (<f,g> / <g,g>) * g
    """
    coeff = inner_product(f, g, a, b, n) / inner_product(g, g, a, b, n)
    return lambda x: coeff * g(x)
