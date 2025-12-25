import math
import pytest
from arca_langlib.arca_interpreter.evaluator import evaluate_expression


def test_binary_transition_exact():
    """Проверка точной записи аксиомы"""
    result = evaluate_expression("(0+1)^2")
    assert result == math.sqrt(2)

def test_binary_transition_with_spaces():
    """Проверка записи с пробелами"""
    result = evaluate_expression(" (0+1)^2 ")
    assert result == math.sqrt(2)

def test_binary_transition_nested_spaces():
    """Проверка записи с пробелами внутри скобок"""
    result = evaluate_expression("( 0 + 1 )^2")
    assert result == math.sqrt(2)

def test_binary_transition_alternative_format():
    """Проверка альтернативной записи"""
    expr = "(0+1) ^ 2"  # пробел перед ^
    result = evaluate_expression(expr)
    assert result == math.sqrt(2)

def test_binary_transition_invalid_expr():
    """Проверка, что другие выражения не интерпретируются как аксиома"""
    expr = "(1+1)^2"
    result = evaluate_expression(expr)
    # Здесь ожидается, что интерпретатор вернёт None или стандартную обработку
    assert result != math.sqrt(2)

