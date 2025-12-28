import pytest
from subprocess import Popen, PIPE
import sys
import json


def run_cli(args):
    """Запуск CLI как отдельного процесса."""
    p = Popen([sys.executable, "-m", "arca_langlib.cli"] + args,
              stdout=PIPE, stderr=PIPE, text=True)
    out, err = p.communicate()
    return p.returncode, out, err


def test_list():
    code, out, err = run_cli(["--list"])
    assert code == 0
    assert "Команды" in out


def test_describe():
    code, out, err = run_cli(["--describe"])
    assert code == 0
    assert "ArcaLang CLI" in out


def test_casus_flat_single():
    code, out, err = run_cli(["--k", "15", "--b", "4"])
    assert code == 0
    assert "Решение" in out


def test_casus_flat_all():
    code, out, err = run_cli(["--k", "15", "--b", "4", "--all-roots"])
    assert code == 0
    assert "Все действительные корни" in out


def test_casus_subcommand():
    code, out, err = run_cli(["casus", "15", "4"])
    assert code == 0
    assert "Решение" in out


def test_eval_dsl():
    code, out, err = run_cli(["eval", "casus(15,4)"])
    assert code == 0
    assert "DSL" in out
