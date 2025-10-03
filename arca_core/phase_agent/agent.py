import yaml
from datetime import datetime

def update_phase_log(agent):
    log_path = "phase_agent/phase_log.yaml"
    try:
        with open(log_path) as f:
            log_data = yaml.safe_load(f) or {}
    except FileNotFoundError:
        log_data = {}

    decision, metric, threshold = agent.inclusion_condition()
    entry = {
        "object_id": agent.object_id,
        "timestamp": datetime.now().isoformat(),
        "parameters": {
            "psi_obj": agent.psi_obj,
            "psi_glob": agent.psi_glob,
            "omega": agent.omega,
            "rho": agent.rho
        },
        "inclusion_metric": round(metric, 4),
        "threshold": round(threshold, 4),
        "inclusion_decision": decision,
        "status": "✅ Включение разрешено" if decision else "⛔ Включение отклонено"
    }

    log_data[agent.object_id] = entry

    with open(log_path, "w") as f:
        yaml.dump(log_data, f, allow_unicode=True)

    agent = PhaseAgent(psi_obj=0.82, psi_glob=1.45, omega=0.12, rho=0.09, object_id="ψ_Arctur_001")
    update_phase_log(agent)

    if __name__ == "__main__":
    agent = PhaseAgent(
        psi_obj=0.82,
        psi_glob=1.45,
        omega=0.12,
        rho=0.09,
        object_id="ψ_Arctur_001"
    )
    update_phase_log(agent)
    print(agent.act())

 