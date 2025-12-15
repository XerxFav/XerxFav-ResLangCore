"""
Первичный тестовый сценарий для проверки OctaveBridge и BoostBridge
в едином пайплайне ArcaLang/Dutrimxord.
"""

import math
import ctypes
import pytest

from arca_langlib.bridges.octave_bridge import OctaveBridge
from arca_langlib.runtime.pipeline import Pipeline


def test_octave_bridge_basic():
    """
    Проверка вызова Octave-функции sin(pi/4).
    """
    bridge = OctaveBridge()
    result = bridge.run("sin(pi/4)")
    # Ожидаемое значение ~ 0.7071
    assert abs(result - math.sqrt(2)/2) < 1e-6
    bridge.close()


def test_boost_bridge_matrix_multiplication():
    """
    Проверка умножения матриц через BoostBridge.
    """
    pipe = Pipeline()

    # Матрицы 2x2
    A = [1.0, 2.0,
         3.0, 4.0]
    B = [5.0, 6.0,
         7.0, 8.0]

    result = pipe.run_boost_matrix(A, B, 2)

    # Результат должен быть [19, 22, 43, 50]
    expected = [19.0, 22.0,
                43.0, 50.0]

    assert all(abs(r - e) < 1e-6 for r, e in zip(result, expected))


def test_pipeline_octave_and_boost():
    """
    Проверка, что оба моста работают в одном пайплайне.
    """
    pipe = Pipeline()

    # Octave: sin(pi/4)
    res_octave = pipe.run_octave("sin(pi/4)")
    assert abs(res_octave - math.sqrt(2)/2) < 1e-6

    # Boost: умножение матриц
    A = [1.0, 0.0,
         0.0, 1.0]
    B = [2.0, 3.0,
         4.0, 5.0]

    res_boost = pipe.run_boost_matrix(A, B, 2)
    # Должно совпадать с B (так как A — единичная матрица)
    assert all(abs(r - e) < 1e-6 for r, e in zip(res_boost, B))
