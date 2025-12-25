from arca_langlib.Phase.runtime import phase_step, Cell


class PhaseBackend:
    """
    Backend интерпретатора для выполнения фазовых операторов.
    """

    def __init__(self):
        self.cells = {}

    def create_cell(self, name, psi0, E, V):
        self.cells[name] = Cell(psi0=psi0, E=E, V=V)
        return self.cells[name]

    def step(self, name, Psi_glob, A, dx, dy, dz, sigma, eps):
        cell = self.cells[name]

        result = phase_step(
            E=cell.E,
            psi0=cell.psi0,
            Psi_glob=Psi_glob,
            A=A,
            dx=dx, dy=dy, dz=dz,
            sigma=sigma,
            eps=eps
        )

        cell.E = result["E"]
        cell.V = result["deltaV"]
        cell.psi0 = result["psi0"]

        return result

    def get_state(self, name):
        cell = self.cells[name]
        return {
            "psi0": cell.psi0,
            "E": cell.E,
            "V": cell.V
        }
