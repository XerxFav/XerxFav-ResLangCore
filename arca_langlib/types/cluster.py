# arca_langlib/types/cluster.py
# Класс Cluster — управляет множественными протоформами

class Cluster:
    """
    Cluster — контейнер для протоформ.
    Позволяет добавлять элементы и выполнять базовые операции над ними.
    """

    def __init__(self):
        self.items = []

    def add(self, protoform):
        """Добавить протоформу в кластер"""
        self.items.append(protoform)

    def size(self) -> int:
        """Вернуть количество элементов в кластере"""
        return len(self.items)

    def clear(self):
        """Очистить кластер"""
        self.items = []
