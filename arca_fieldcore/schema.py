#arca_fieldcore/schema.py — фазовая онтология
# schema.py — фазовые типы и допустимые переходы

PHASE_TYPES = ["neutral", "positive", "negative"]

TRANSITIONS = {
    "neutral": ["positive", "negative"],
    "positive": ["neutral", "negative"],
    "negative": ["neutral", "positive"]
}

def is_valid_transition(from_phase: str, to_phase: str) -> bool:
    """Проверяет, допустим ли переход между фазами"""
    return to_phase in TRANSITIONS.get(from_phase, [])
#📌 Это основа для CI, интерпретатора и генератора фазовых карт.