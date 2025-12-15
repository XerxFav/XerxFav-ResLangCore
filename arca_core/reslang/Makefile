CXX = g++
CXXFLAGS = -std=c++23 -O2 -Wall -I./include
LDFLAGS = -lboost_system -lboost_filesystem -lboost_program_options -lboost_serialization

SRC = $(wildcard src/*.cpp) \
	$(wildcard src/compiler/*.cpp)

OBJ = $(SRC:.cpp=.o)
TARGET = reslang

# 🧩 Фаза 0: Сборка ядра
all: $(TARGET)

$(TARGET): $(OBJ)
	$(CXX) $(OBJ) -o $(TARGET) $(LDFLAGS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# 🌀 Фаза 1: Генерация документации
doc-gen:
	@echo "[doc-gen] Генерация README и phase_report.md..."
	python3 resci.py --doc --output docs/phase_report.md

# 🧪 Фаза 2: Запуск тестов
test-run:
	@echo "[test-run] Запуск тернарных и фазовых тестов..."
	$(CXX) tests/test_ternary.cpp -o test_ternary $(CXXFLAGS)
	./test_ternary

# 🌐 Фаза 3: Отчет о фазах CI
phase-report:
	@echo "[phase-report] CI-фаза: анализ структуры и миграций..."
	python3 resci.py --ci --output phase_report.md

# 🧹 Фаза 4: Очистка
clean:
	rm -f $(OBJ) $(TARGET) test_ternary docs/phase_report.md

# 🧠 Фаза 5: Проверка типов и синтаксиса
type-check:
	@echo "[type-check] Проверка типов, пространств имён и синтаксиса..."
	@for file in $(SRC); do \
	echo "  ⮕ Проверка $$file"; \
	$(CXX) $(CXXFLAGS) -fsyntax-only $$file; 
	done


#🧠 Онтологическая интерпретация фаз
#Фаза	Цель	Онтологический смысл
#all	Сборка ядра	Манифестация языка как исполнимой сущности
#doc-gen	Документация	Рефлексия и самосознание системы
#test-run	Тестирование логики	Проверка когерентности тернарных и фазовых аксиом
#phase-report	CI-отчет	Историзация и фазовая запись эволюции
#clean	Очистка	Акт очищения и подготовки к новой фазе