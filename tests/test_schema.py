#🔹 tests/test_schema.py — покрытие фазовых правил

# test_schema.py — тесты для фазовых переходов
#Добавить параметризацию:
import pytest

@pytest.mark.parametrize("from_phase,to_phase,expected", [
    ("neutral", "positive", True),
    ("positive", "neutral", True),
    ("negative", "positive", True),
    ("positive", "undefined", False),
    ("neutral", "neutral", False),
])
def test_phase_transitions(from_phase, to_phase, expected):
    assert schema.is_valid_transition(from_phase, to_phase) == expected
    
    #📌 Это делает тест компактным и расширяемым.

from arca_fieldcore import schema
#Добавить фазовую маркировку:
#@pytest.mark.phase
#def test_valid_transitions():

#📌 Позволяет запускать фазовые тесты отдельно: pytest -m phase

def test_valid_transitions():
    assert schema.is_valid_transition("neutral", "positive")
    assert schema.is_valid_transition("positive", "neutral")
    assert schema.is_valid_transition("negative", "positive")

def test_invalid_transition():
    assert not schema.is_valid_transition("positive", "undefined")
    assert not schema.is_valid_transition("neutral", "neutral")
#📌 Можно расширить параметризацией и фазовыми маркерами.

#Если ты хочешь убедиться, что test_schema.py точно выполняется, можно добавить фазовую маркировку:
#- name: Run schema tests
#run: |
#pytest tests/test_schema.py --cov=arca_fieldcore --cov-report=term
