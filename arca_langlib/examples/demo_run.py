from arca_langlib.runtime.agent import load_agent_from_template


def main():
    template_path = (
        "/home/arca/ResLang/ArcaLang/arca_langlib/templates/agent_template.yaml"
    )
    agent = load_agent_from_template(template_path)

    inputs = {"input1": "ArcaLang"}
    result = agent.run_phase("example_phase", inputs)

    print("Результат выполнения фазы:")
    print(result)

    status = agent.get_status("example_phase")
    print(f"Статус фазы: completed ")


if __name__ == "__main__":
    main()
