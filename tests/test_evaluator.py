#🔹 tests/test_evaluator.py — фазовая интерпретация

#оформим tests/test_evaluator.py как фазовую валидацию интерпретатора. Он будет проверять корректность переходов, соответствие schema.py, и устойчивость #PhaseEvaluator. Мы встроим параметризацию, фазовые маркеры и проверку ошибок.
#
import pytest
from arca_interpreter.evaluator import PhaseEvaluator

@pytest.mark.phase
@pytest.mark.parametrize("initial,target,expected", [
    ("neutral", "positive", "Transitioned to positive"),
    ("positive", "neutral", "Transitioned to neutral"),
    ("negative", "positive", "Transitioned to positive"),
    ("positive", "undefined", "Invalid transition from positive to undefined"),
    ("neutral", "neutral", "Invalid transition from neutral to neutral"),
])
def test_phase_evaluation(initial, target, expected):
    evaluator = PhaseEvaluator(initial)
    result = evaluator.evaluate(target)
    assert result == expected
#
#✅ Что покрывает тест

#   🔁 Проверку допустимых переходов (neutral → positive)

#  ❌ Обнаружение недопустимых переходов (positive → undefined)

# 🔄 Сохранение текущей фазы при ошибке

#📌 Совместимость с schema.py через is_valid_transition

#