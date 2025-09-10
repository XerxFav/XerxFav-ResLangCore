from enum import Enum

class PhaseBit(Enum):
    QND = 0
    PHASE = 1
    ACT = 2

QND = (1 / (9.11e-31 * 299_792_458**2)) ** (1/3)
