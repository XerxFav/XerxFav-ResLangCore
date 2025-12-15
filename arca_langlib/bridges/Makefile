# Makefile для ArcaLang/Dutrimxord: сборка BoostBridge, установка зависимостей, тесты, визуализация и запуск циклов

CXX = g++
CXXFLAGS = -O2 -fPIC -shared
INCLUDES = -I/usr/include
LIBS = -L/usr/lib/x86_64-linux-gnu -lboost_system -lboost_atomic

TARGET = boost_bridge.so
SRC = boost_bridge.cpp
INSTALL_DIR = /usr/lib/x86_64-linux-gnu

# ==========================
# Основные цели
# ==========================

# Сборка boost_bridge.so
all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $(SRC) -o $(TARGET) $(INCLUDES) $(LIBS)

# Очистка
clean:
	rm -f $(TARGET)

# Принудительная пересборка
rebuild: clean all

# ==========================
# Установка и зависимости
# ==========================

# Установка boost_bridge.so глобально
install: $(TARGET)
	sudo cp $(TARGET) $(INSTALL_DIR)/$(TARGET)
	sudo ldconfig

# Установка Python-зависимостей
deps:
	pip install --upgrade pip
	pip install pytest oct2py numpy scipy plotly
	
octave-bridge:
	pip install oct2py
	python3 -m py_compile octave_bridge.py



# ==========================
# Тесты и визуализация
# ==========================

# Запуск тестов pytest

	
	


# Демонстрация визуализации (heatmap через Plotly)
viz:
	python3 -c "from arca_langlib.runtime.visualizer import Visualizer; Visualizer.heatmap([[1,2,3],[4,5,6],[7,8,9]], title='Demo Heatmap')"
	

octave-bridge:
	python3 -m py_compile octave_bridge.py


# ==========================
# Циклы фазовых переходов
# ==========================

# Запуск модуля cycle_manager.py
cycle:
	python3 ../runtime/cycle_manager.py
	
	# ==========================
# CI/CD полный цикл
# ==========================
ci: clean clean-doc deps bridges-all test doc

