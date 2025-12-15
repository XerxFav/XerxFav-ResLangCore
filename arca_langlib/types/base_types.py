class ArcaValue:
    def __init__(self, value, type_name):
        self.value = value
        self.type = type_name

    def __repr__(self):
        return f"<{self.type}:{self.value}>"
