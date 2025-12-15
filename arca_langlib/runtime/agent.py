from arca_langlib.runtime.memory import MemoryStore
from arca_langlib.runtime.interpreter import evaluate
from arca_langlib.types.phase_types import PhaseSignature, PhaseStatus
from enum import Enum
import os
import yaml
def load_agent_from_template(path: str = None):
    """
    Загружает агент из YAML-шаблона.
    Если путь не указан, возвращает заглушку.
    """
    if path is None:
        return {"agent": {"name": "DummyAgent"}}

    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        return data
    except Exception:
        return {"agent": {"name": "❓"}}


def test_load_agent_from_template_default():
    agent = load_agent_from_template()
    assert "agent" in agent
    assert "name" in agent["agent"]

def test_load_agent_from_template_file(tmp_path):
    f = tmp_path / "agent.yaml"
    f.write_text("agent:\n  name: TestAgent")
    agent = load_agent_from_template(str(f))
    assert agent["agent"]["name"] == "TestAgent"

def test_load_agent_from_template_invalid_file(tmp_path):
    f = tmp_path / "broken.yaml"
    f.write_text("not: valid: yaml:::")
    agent = load_agent_from_template(str(f))
    assert agent["agent"]["name"] == "❓"

class PhaseStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class PhaseAgent:
    """Фазовый агент ArcaLang: управляет фазами, памятью и выполнением логики."""

    def __init__(self, name="default_agent"):
        self.name = name
        self.memory = MemoryStore()
        self.phases = {}

    def register_phase(self, signature: PhaseSignature, logic_fn):
        self.phases[signature.name] = {
            "signature": signature,
            "logic": logic_fn,
            "status": PhaseStatus.PENDING,
        }
        print(f"[Agent:{self.name}] Registered phase: {signature.name}")

    def run_phase(self, phase_name, inputs):
        phase = self.phases.get(phase_name)
        if not phase:
            raise ValueError(f"Phase '{phase_name}' not found")

        print(f"[Agent:{self.name}] Running phase: {phase_name}")
        phase["status"] = PhaseStatus.RUNNING

        context = {**inputs, "memory": self.memory}
        result = phase["logic"](context)

        phase["status"] = PhaseStatus.COMPLETED
        print(f"📊 Статус: {self.get_status(phase_name).value}")

        return result

    def get_status(self, phase_name):
        phase = self.phases.get(phase_name)
        if not phase:
            return PhaseStatus.FAILED
        return phase["status"]

    def load_phase_from_yaml(path):
        """Загружает фазу из YAML-шаблона и возвращает сигнатуру и функцию логики."""
        if not os.path.exists(path):
            raise FileNotFoundError(f"Phase file not found: {path}")
        try:
            with open(path, "r") as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parsing error in {path}: {e}")

        phase = data.get("phase", {})
        name = phase.get("name", "unnamed_phase")
        inputs = [(inp["name"], inp["type"]) for inp in phase.get("inputs", [])]
        outputs = [(out["name"], out["type"]) for out in phase.get("outputs", [])]
        logic_code = phase.get("logic", "")

    def logic_fn(ctx):
        input1 = ctx.get("input1", "")
        return {
            "result": len(input1)
        }  # Пример: заменить на eval(logic_code) при расширении

        signature = PhaseSignature(name, inputs, outputs)
        return signature, logic_fn

    def load_agent_from_template(template_path):
        """Создаёт фазового агента на основе YAML-шаблона агента."""
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Agent template not found: {template_path}")
        try:
            with open(template_path, "r") as f:
                agent_data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parsing error in {template_path}: {e}")

        agent_name = agent_data.get("agent", {}).get("name", "default_agent")
        agent = PhaseAgent(agent_name)

        for phase_info in agent_data.get("agent", {}).get("phases", []):
            template_file = phase_info.get("template")
            if not template_file:
                continue  # пропустить фазу без шаблона

            if not os.path.exists(template_file):
                template_file = os.path.join("templates", template_file)

            signature, logic_fn = load_phase_from_yaml(template_file)
            agent.register_phase(signature, logic_fn)
        return agent
