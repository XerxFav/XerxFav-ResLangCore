import yaml
from datetime import datetime
from phase_agent.agent import PhaseAgent, update_phase_log

# 📦 Исходные объекты
objects = [
    {
        "object_id": "ψ_Arctur_001",
        "psi_obj": 0.82,
        "psi_glob": 1.45,
        "omega": 0.12,
        "rho": 0.09
    },
    {
        "object_id": "ψ_ArcaLang_Core",
        "psi_obj": 0.76,
        "psi_glob": 1.32,
        "omega": 0.10,
        "rho": 0.08
    },
    {
        "object_id": "ψ_ResLang_Node",
        "psi_obj": 0.51,
        "psi_glob": 1.20,
        "omega": 0.14,
        "rho": 0.11
    }
]

# 📊 Генерация phase_map.yaml
phase_map = []
for obj in objects:
    agent = PhaseAgent(**obj)
    decision, metric, threshold = agent.inclusion_condition()
    update_phase_log(agent)
    phase_map.append({
        "object_id": obj["object_id"],
        "psi_obj": obj["psi_obj"],
        "psi_glob": obj["psi_glob"],
        "omega": obj["omega"],
        "rho": obj["rho"],
        "inclusion_metric": round(metric, 4),
        "threshold": round(threshold, 4),
        "inclusion_decision": decision,
        "status": "✅ Включение разрешено" if decision else "⛔ Включение отклонено"
    })

with open("phase_agent/phase_map.yaml", "w") as f:
    yaml.dump({"phase_map": phase_map}, f, allow_unicode=True)

print("✅ Документация CI-агента обновлена.")
