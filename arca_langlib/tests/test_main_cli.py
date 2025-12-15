import subprocess
import sys
import pytest

CLI = [sys.executable, "-m", "arca_langlib.cli"]

def run_cli(args):
    """Запуск CLI и возврат (код выхода, stdout, stderr)."""
    result = subprocess.run(
        CLI + args,
        capture_output=True,
        text=True
    )
    return result.returncode, result.stdout, result.stderr

def test_main_cli_help():
    code, out, err = run_cli(["--help"])
    assert code == 0
    assert "usage" in out.lower() or "help" in out.lower()

@pytest.mark.parametrize("arg", ["--list", "--describe"])
def test_main_cli_commands(arg):
    code, out, err = run_cli([arg])
    assert code == 0
    assert out.strip() != ""

def test_main_cli_auto_single_root():
    code, out, err = run_cli(["--k", "15", "--b", "4", "--mode", "auto"])
    assert code == 0
    assert "Решение" in out or "root" in out.lower()

def test_main_cli_auto_all_roots():
    code, out, err = run_cli(["--k", "15", "--b", "4", "--mode", "auto", "--all-roots"])
    assert code == 0
    assert "Все действительные корни" in out or "roots" in out.lower()
    # Проверим, что в выводе есть 4 и -2
    assert "4.0" in out
    assert "-2.0" in out

def test_main_cli_trig_mode():
    code, out, err = run_cli(["--k", "15", "--b", "4", "--mode", "trig"])
    assert code == 0
    assert "Тригонометрическая форма" in out or "trig" in out.lower()
    # Проверим, что в выводе есть 4 и -2
    assert "4.0" in out
    assert "-2.0" in out
