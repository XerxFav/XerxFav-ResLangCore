from .phase import PhaseBit, QND

class Chronotope:
    def __init__(self):
        self.tau = QND
        self.state = PhaseBit.QND
        self.morphisms = []
