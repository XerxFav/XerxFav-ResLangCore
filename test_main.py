import os
import runpy
import yaml
import tempfile
from arca_langlib.__main__ import list_templates, describe_templates

def test_list_templates(tmp_path):
    # создаём временные YAML-файлы
    f1 = tmp_path / "agent1.yaml"
    f1.write_text("agent:\n  name: TestAgent1")
    f2 = tmp_path / "agent2.yaml"
    f2.write_text("agent:\n  name: TestAgent2")

    files = list_templates(directory=str(tmp_path))
    assert "agent1.yaml" in files
    assert "agent2.yaml" in files

def test_describe_templates(tmp_path):
    f1 = tmp_path / "agent1.yaml"
    f1.write_text("agent:\n  name: TestAgent1")
    f2 = tmp_path / "agent2.yaml"
    f2.write_text("agent:\n  name: TestAgent2")

    descriptions = describe_templates(directory=str(tmp_path))
    # проверяем, что имена агентов извлекаются
    assert any("TestAgent1" in str(d) for d in descriptions)
    assert any("TestAgent2" in str(d) for d in descriptions)

def test_main_entrypoint_runs():
    # smoke‑тест: модуль запускается без ошибок
    runpy.run_module("arca_langlib.__main__", run_name="__main__")
