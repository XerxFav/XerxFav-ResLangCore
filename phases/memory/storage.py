class ChronoStorage:
    def __init__(self):
        self.data = []

    def save(self, chronotope: dict):
        self.data.append(chronotope)
