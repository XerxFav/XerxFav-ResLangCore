# arca_langlib/runtime/pipeline.py
from arca_langlib.bridges.octave_bridge import OctaveBridge
import ctypes

class Pipeline:
    def __init__(self):
        self.octave = OctaveBridge()
        self.boost = ctypes.CDLL("./boost_bridge.so")

    def run_octave(self, expr: str):
        return self.octave.run(expr)

    def run_boost_matrix(self, A, B, n):
        C = (ctypes.c_double * (n*n))()
        self.boost.multiply_matrix(
            (ctypes.c_double * (n*n))(*A),
            (ctypes.c_double * (n*n))(*B),
            C,
            n
        )
        return list(C)
