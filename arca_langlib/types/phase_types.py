class PhaseSignature:
    def __init__(self, name, inputs, outputs):
        self.name = name
        self.inputs = inputs  # List of (name, type)
        self.outputs = outputs  # List of (name, type)

    def describe(self):
        return {
            "name": self.name,
            "inputs": self.inputs,
            "outputs": self.outputs
        }

class PhaseStatus:
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
class PhaseAgent:
    """Фазовый агент ArcaLang: управляет фазами, памятью и выполнением логики."""
