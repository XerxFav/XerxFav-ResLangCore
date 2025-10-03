import shutil
import os
from phase_agent.agent import PhaseAgent, update_phase_log

def migrate_phase_object(object_id):
    src = f"/home/arca/ResLang/ArcaLang/phase_agent/export/{object_id}.yaml"
    dst = f"/home/arca/XerxFav-ResLangCore/phase_agent/import/{object_id}.yaml"
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"✅ Миграция {object_id} завершена.")
    else:
        print(f"⛔ Объект {object_id} не найден.")

from phase_agent.agent import PhaseAgent, update_phase_log

def migrate_and_log(object_id, psi_obj, psi_glob, omega, rho):
    agent = PhaseAgent(psi_obj, psi_glob, omega, rho, object_id)
    update_phase_log(agent)
    # Здесь можно добавить миграцию файлов между ArcaLang и ResLangCore
    print(f"Фазовое решение: {agent.act()}")

