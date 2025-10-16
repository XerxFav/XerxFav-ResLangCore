# 🧠 Основные переменные
PYTHON=python3
VENV=.venv/bin/activate
SCRIPTS_DIR=scripts
TESTS_DIR=tests
PHASES_DIR=phases
DOCS_DIR=docs
REPORTS_DIR=reports
RESCI=$(SCRIPTS_DIR)/resci.py
AUDIT=$(SCRIPTS_DIR)/arca_phase_audit.py

# 🧼 Очистка временных файлов
clean:
	rm -rf __pycache__ .pytest_cache *.pyc *.swp $(REPORTS_DIR)/*.md $(DOCS_DIR)/*.svg

# 📦 Установка зависимостей
install:
	$(PYTHON) -m pip install -r requirements.txt

# 🧪 Запуск тестов
test:
	$(PYTHON) -m pytest $(TESTS_DIR)

# 🧭 Фазовая сборка
phase-build:
	@echo "🔧 Сборка фазовых компонентов..."
	@find $(PHASES_DIR) -name '*.py' -exec $(PYTHON) {} \;

# 📜 Аудит фаз и генерация diff_report.md
audit:
	@echo "📋 Запуск фазового аудита..."
	$(PYTHON) $(AUDIT)
	@echo "📑 Генерация diff_report.md..."
	@bash scripts/gen_diff_report.sh

# 🧠 Генерация phase_report.md и SVG-графики
report:
	@echo "📊 Генерация phase_report.md и SVG..."
	$(PYTHON) $(RESCI)

# 🧼 Очистка и восстановление после сбоя
recover:
	@vim -r Makefile

purge-swp:
	rm -f .Makefile.swp

# 🧬 CI: запуск фазового CI и обновление отчётов
ci:
	@echo "🚀 Запуск CI фаз..."
	@make audit
	@make report
	@make test
	@make arca_core_phase1

# 📁 Сборка документации
docs:
	@echo "📚 Сборка документации..."
	@pandoc README.md -o $(DOCS_DIR)/README.pdf
	@pandoc $(REPORTS_DIR)/phase_report.md -o $(DOCS_DIR)/phase_report.pdf

# 🧩 Фазовая верификация коммитов
verify-commits:
	@echo "🔍 Проверка фазовых меток коммитов..."
	@git log --pretty=format:"%h %s" | grep -E 'phase_[0-9]+'

# 🧠 Автоматическая генерация фазовых Make-команд
generate-make-phase:
	@echo "⚙️ Генерация фазовых целей Makefile..."
	@python3 scripts/gen_make_phases.py > Makefile.phases

# 🔁 Обновление README и phase_report
update-readme:
	@echo "📝 Обновление README.md и phase_report.md..."
	@python3 scripts/update_readme.py
	@make report

.PHONY: clean install test phase-build audit report recover purge-swp ci docs verify-commits generate-make-phase update-readme

# 🔗 Подключение фазовых целей
include Makefile.phases
arca_core_phase1:
	@echo "🚀 Запуск Python-фазы arca_core_phase1..."
	@find arca_core/phase1 -name '*.py' -exec $(PYTHON) {} \;
test_phase1:
	$(PYTHON) -m pytest tests/arca_core_phase1
arca_core_objects = phase_types.o phase_utils.o

arca_core_phase2: src/ternary.cpp src/phase_types.cpp src/phase_utils.cpp
	$(CXX) $(CXXFLAGS) -o bin/arca_core_phase2 $^ -lboost_system

phase_migrate:
	bash arca-full-migrate.sh

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




