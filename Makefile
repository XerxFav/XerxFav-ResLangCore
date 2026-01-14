# ============================================================
# ArcaLang — Disciplinary Makefile
# ============================================================

.PHONY: deps install install-core install-ml install-viz install-extras install-all \
	test coverage lint format doc serve-doc clean clean-doc doc-pdf changelog \
	metapysics-diagrams diagrams cycle viz serve bridges-all boost-bridge \
	octave-bridge all dev ci audit audit-lib artifacts

# ------------------------------------------------------------
# Dependencies
# ------------------------------------------------------------

deps:
		pip install pdoc watchdog flake8 black isort fastapi uvicorn flask pytest coverage

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

install:
		pip install -e .

sync-reqs:
		cp requirements/all.txt requirements.txt

# ------------------------------------------------------------
# Bridges
# ------------------------------------------------------------

boost-bridge:
		$(MAKE) -C arca_langlib/bridges all

octave-bridge:
		$(MAKE) -C arca_langlib/bridges octave-bridge

bridges-all: boost-bridge octave-bridge

# ------------------------------------------------------------
# Testing & Coverage
# ------------------------------------------------------------

test: bridges-all
		pytest arca_langlib/tests -v

coverage:
		pytest --cov=arca_langlib --cov-report=term-missing --cov-report=html

# ------------------------------------------------------------
# Linting & Formatting
# ------------------------------------------------------------

lint:
		flake8 arca_langlib
		black --check arca_langlib
		isort --check-only arca_langlib

format:
		black arca_langlib
		sort arca_langlib

# ------------------------------------------------------------
# Documentation
# ------------------------------------------------------------

doc:
		pdoc --html arca_langlib --output-dir docs --force

serve-doc:
		python3 -m http.server --directory docs/ 8080

clean-doc:
		rm -rf docs/

doc-pdf:
		ENABLE_PDF_EXPORT=1 mkdocs build

changelog:
		mkdir -p docs
		python3 scripts/generate_changelog.py

# ------------------------------------------------------------
# Diagrams
# ------------------------------------------------------------

metapysics-diagrams:
		dot -Tsvg docs/metapysics/assets/diagrams/metapysics_dependencies.dot \
		-o docs/metapysics/assets/diagrams/metapysics_dependencies.svg

diagrams:
		@echo "Generating all MetaPhysics diagrams..."
		@for f in docs/metapysics/assets/diagrams/*.dot; do \
		svg="$${f%.dot}.svg"; \
		echo "  → $$svg"; \
		dot -Tsvg "$$f" -o "$$svg"; \
		done
		@echo "Done."

# ------------------------------------------------------------
# Runtime & Visualization
# ------------------------------------------------------------

cycle:
		python3 arca_langlib/runtime/cycle_manager.py

viz:
		python3 -c "from arca_langlib.runtime.visualizer import Visualizer; Visualizer.heatmap([[1,2,3],[4,5,6],[7,8,9]], title='Demo Heatmap')"

serve:
		uvicorn arca_langlib.runtime.app:app --reload --host 0.0.0.0 --port 8000

# ------------------------------------------------------------
# Cleanup
# ------------------------------------------------------------

clean:
		rm -rf build dist *.egg-info
		rm -rf .pytest_cache .coverage htmlcov
		find . -name "__pycache__" -type d -exec rm -rf {} +

# ------------------------------------------------------------
# Full cycles
# ------------------------------------------------------------

all: deps bridges-all test coverage doc metapysics-diagrams

dev:
	watchmedo shell-command \
		--patterns="*.py" 
		--recursive \
		--command='make test && make doc'

# ------------------------------------------------------------
# CI Pipeline
# ------------------------------------------------------------

ci: clean clean-doc deps changelog bridges-all test coverage doc doc-pdf audit audit-lib artifacts

# ------------------------------------------------------------
# Audits
# ------------------------------------------------------------

audit:
		python3 scripts/arca_phase_audit.py

audit-lib:
		python3 scripts/arca_library_audit.py
		@grep "Overall docstring coverage" ci/library_audit.md | awk '{print $$5}' | sed 's/%//' | \
		awk '{ if ($$1 < 80) { print "⚠️ Coverage below 80%"; exit 1 } }'

# ------------------------------------------------------------
# Artifacts
# ------------------------------------------------------------

artifacts:
		@echo "Artifacts step placeholder (PDF, logs, diagrams)"
