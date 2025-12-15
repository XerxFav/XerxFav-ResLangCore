import math
import pytest
from arca_langlib.casus_reducibilis import (
    phi,
    solve_cubic,
    solve_cubic_trig,
    solve_cubic_trig_all,
    resolve_casus_irreducibilis
)

def test_phi_bombelli():
    # Пример Бомбелли: x^3 = 15x + 4 → Φ = 4 - 125 = -121
    assert math.isclose(phi(15, 4), -121.0, rel_tol=1e-12)

def test_cardano_bombelli():
    x = solve_cubic(15, 4)
    assert math.isclose(x**3, 15*x + 4, rel_tol=1e-9)

def test_trig_bombelli_single():
    x = solve_cubic_trig(15, 4)
    assert math.isclose(x, 4.0, rel_tol=1e-9)
    assert math.isclose(x**3, 15*x + 4, rel_tol=1e-9)

def test_trig_bombelli_all():
    roots = solve_cubic_trig_all(15, 4)
    # Должны быть три корня: [4, -2, -2]
    assert len(roots) == 3
    for r in roots:
        assert math.isclose(r**3, 15*r + 4, rel_tol=1e-9)

def test_resolve_auto_single():
    x = resolve_casus_irreducibilis(15, 4)
    assert math.isclose(x, 4.0, rel_tol=1e-9)

def test_resolve_auto_all():
    roots = resolve_casus_irreducibilis(15, 4, all_roots=True)
    assert isinstance(roots, list)
    assert len(roots) == 3
    for r in roots:
        assert math.isclose(r**3, 15*r + 4, rel_tol=1e-9)

@pytest.mark.parametrize("k,b", [(3,0), (9,1), (12,-5), (0,2)])
def test_general_consistency(k,b):
    # Проверка: любой корень должен удовлетворять уравнению
    result = resolve_casus_irreducibilis(k, b, all_roots=True)
    if isinstance(result, list):
        for x in result:
            assert math.isclose(x**3, k*x + b, rel_tol=1e-7, abs_tol=1e-7)
    else:
        assert math.isclose(result**3, k*result + b, rel_tol=1e-7, abs_tol=1e-7)
