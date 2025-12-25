def algometric_invariant(C: float, L: float, U: float, A: float) -> bool:
    """
    Алгометрический инвариант:
    C/L = U/A
    """
    return (C / L) == (U / A)
