# ==========================
# Корневой Makefile для ArcaLang/Dutrimxord
# ==========================

.PHONY: deps install test coverage lint format doc serve-doc clean clean-doc cycle viz serve bridges-all ci dev all

# Установка зависимостей
deps:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install pdoc watchdog flake8 black isort fastapi uvicorn flask pytest coverage
.PHONY: install-core install-ml install-viz install-extras install-all

install-core:
	pip install -r requirements/core.txt

install-ml:
	pip install -r requirements/ml.txt

install-viz:
	pip install -r requirements/viz.txt

install-extras:
	pip install -r requirements/extras.txt

install-all:
	pip install -r requirements/all.txt
sync-reqs:
	cp requirements/all.txt requirements.txt

# Установка пакета в editable-режиме
install:
	pip install -e .

# Сборка мостов
boost-bridge:
	$(MAKE) -C arca_langlib/bridges all

octave-bridge:
	$(MAKE) -C arca_langlib/bridges octave-bridge

bridges-all: boost-bridge octave-bridge

# Тесты (только unit-тесты библиотеки)
test: bridges-all
	pytest arca_langlib/tests -v


# Запуск покрытия
coverage:
	pytest --cov=arca_langlib --cov-report=term-missing --cov-report=html

# Линтинг и автоформатирование
lint:
	flake8 arca_langlib
	black --check arca_langlib
	isort --check-only arca_langlib

format:
	black arca_langlib
	isort arca_langlib

# Документация
doc:
	pdoc --html arca_langlib --output-dir docs --force

serve-doc:
	python3 -m http.server --directory docs/ 8080

clean-doc:
	rm -rf docs/

# Очистка артефактов
clean:
	rm -rf build dist *.egg-info
	rm -rf .pytest_cache .coverage htmlcov
	find . -name "__pycache__" -type d -exec rm -rf {} +

# Циклы фазовых переходов
cycle:
	python3 arca_langlib/runtime/cycle_manager.py

# Визуализация
viz:
	python3 -c "from arca_langlib.runtime.visualizer import Visualizer; Visualizer.heatmap([[1,2,3],[4,5,6],[7,8,9]], title='Demo Heatmap')"

# Локальный сервер приложения
serve:
	uvicorn arca_langlib.runtime.app:app --reload --host 0.0.0.0 --port 8000

# Полный цикл
all: deps bridges-all test coverage doc

# Режим разработки
dev:
	watchmedo shell-command \	
		--patterns="*.py" \
		--recursive \
		--command='make test && make doc'

# CI/CD полный цикл
ci: clean clean-doc deps bridges-all test coverage doc audit audit-lib

audit:
	python3 scripts/arca_phase_audit.py

.PHONY: audit audit-lib

audit:
	python3 scripts/arca_phase_audit.py

audit-lib:
	python3 scripts/arca_library_audit.py
	@grep "Overall docstring coverage" ci/library_audit.md | awk '{print $$5}' | sed 's/%//' | \
		awk '{ if ($$1 < 80) { print "⚠️ Coverage below 80%"; exit 1 } }'


