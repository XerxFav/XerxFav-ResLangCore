from arca_core.phase import PhaseBit, QND

def evaluate_impulse(impulse: float) -> PhaseBit:
    if impulse < QND:
        return PhaseBit.QND
    elif impulse == QND:
        return PhaseBit.PHASE
    else:
        return PhaseBit.ACT
class PhaseEvaluator:
    def __init__(self, initial_phase):
        self.current = initial_phase
        self.history = [initial_phase]

    def evaluate(self, target_phase):
        from schema import is_valid_transition
        if is_valid_transition(self.current, target_phase):
            self.current = target_phase
            self.history.append(target_phase)
            return f"Transitioned to {target_phase}"
        else:
            return f"Invalid transition from {self.current} to {target_phase}"

    def run_scenario(self, sequence):
        results = []
        for phase in sequence:
            result = self.evaluate(phase)
            results.append(result)
        return results

        # 📌 Теперь можно запускать сценарии:

#evaluator.run_scenario(["positive", "neutral", "negative"])
