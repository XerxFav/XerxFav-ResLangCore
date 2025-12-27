from dataclasses import dataclass
from enum import Enum
from typing import Any, Tuple


class CategoryMode(str, Enum):
    EVEN = "even_category"
    ODD = "odd_category"


@dataclass(frozen=True)
class ParameterTriple:
    p1: Any
    p2: Any
    p3: Any
    volume: str = "{4πR^3 r^2 (V - V0)}"  # символическая фиксация объёма


def validity_signature(param: Any) -> Any:
    """
    Абстрактная сигнатура валидности ν(P).
    В реальных DSL переопределяется или конкретизируется.
    """
    return param


def classify_category(triple: ParameterTriple) -> CategoryMode:
    """
    Классифицирует тройку (P1, P2, P3) в чётную или нечётную категорию
    по совпадению валидностных сигнатур.
    """
    v12 = (validity_signature(triple.p1), validity_signature(triple.p2))
    v3 = validity_signature(triple.p3)

    if v3 in v12:
        return CategoryMode.EVEN
    return CategoryMode.ODD
