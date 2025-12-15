from arca_langlib.types.base_types import ArcaValue

def evaluate(expression, context):
    # Простейший интерпретатор выражений ArcaLang
    if isinstance(expression, str):
        return ArcaValue(expression.upper(), "string")
    return ArcaValue(expression, "unknown")
