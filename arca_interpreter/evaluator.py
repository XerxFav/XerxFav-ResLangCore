from arca_core.phase import PhaseBit, QND

def evaluate_impulse(impulse: float) -> PhaseBit:
    if impulse < QND:
        return PhaseBit.QND
    elif impulse == QND:
        return PhaseBit.PHASE
    else:
        return PhaseBit.ACT
