from arca_langlib.runtime.agent import load_agent_from_template
import os
import yaml


def list_templates(directory="templates"):
    """Возвращает список YAML-файлов в указанной директории."""
    return [f for f in os.listdir(directory) if f.endswith(".yaml")]


def describe_templates(directory="templates"):
    """Возвращает список шаблонов с описанием агента."""
    files = list_templates(directory)
    descriptions = []
    for f in files:
        path = os.path.join(directory, f)
        try:
            with open(path, "r") as file:
                data = yaml.safe_load(file)
            name = data.get("agent", {}).get("name", "❓")
            desc = data.get("agent", {}).get("description", "Без описания")
            descriptions.append((f, name, desc))
        except Exception:
            descriptions.append((f, "❌", "Ошибка чтения"))
    return descriptions


def validate_agent_template(path):
    """Проверяет, что YAML-файл является корректным шаблоном агента."""
    if not os.path.exists(path):
        print(f"❌ Файл не найден: {path}")
        return False
    try:
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        if not data or "agent" not in data:
            print("⚠️ Выбранный файл не является шаблоном агента.")
            return False
        if not isinstance(data["agent"].get("phases", []), list):
            print("⚠️ В шаблоне агента отсутствует список фаз.")
            return False
        return True
    except yaml.YAMLError as e:
        print(f"❌ Ошибка чтения YAML: {e}")
        return False


def main():
    print("🔷 ArcaLang: Интерактивный запуск фазового агента")

    templates = describe_templates()
    if not templates:
        print("❌ Нет доступных шаблонов в папке 'templates'")
        return

    print("\n📁 Доступные шаблоны агентов:")
    for i, (fname, name, desc) in enumerate(templates):
        print(f"  [{i+1}] {fname} → {name}: {desc}")

    choice = input("🔢 Выберите номер шаблона: ").strip()
    try:
        index = int(choice) - 1
        selected_file = templates[index][0]
    except (ValueError, IndexError):
        print("❌ Неверный выбор шаблона.")
        return

    template_path = os.path.join("templates", selected_file)
    if not validate_agent_template(template_path):
        return

    try:
        agent = load_agent_from_template(template_path)
    except Exception as e:
        print(f"❌ Ошибка загрузки агента: {e}")
        return

    phase_names = list(agent.phases.keys())
    if not phase_names:
        print("⚠️ В агенте нет зарегистрированных фаз.")
        return

    print("\n📌 Доступные фазы:")
    for i, name in enumerate(phase_names):
        print(f"  [{i+1}] {name}")

    selected = input("🔢 Введите номера фаз через запятую (например: 1,3): ").strip()
    try:
        indices = [int(x.strip()) - 1 for x in selected.split(",")]
        selected_phases = [phase_names[i] for i in indices if 0 <= i < len(phase_names)]
    except Exception:
        print("❌ Неверный формат выбора фаз.")
        return

    for phase_name in selected_phases:
        phase = agent.phases[phase_name]
        signature = phase["signature"]

        print(f"\n🧠 Ввод данных для фазы '{phase_name}':")
        inputs = {}
        for input_name, input_type in signature.inputs:
            value = input(f"  🔹 {input_name} ({input_type}): ").strip()
            inputs[input_name] = value

        try:
            print(f"\n🚀 Запуск фазы '{phase_name}'...")
            result = agent.run_phase(phase_name, inputs)
            print("✅ Результат:")
            print(result)
            print(f"📊 Статус: {agent.get_status(phase_name)}")
        except Exception as e:
            print(f"❌ Ошибка выполнения фазы '{phase_name}': {e}")


if __name__ == "__main__":
    main()
