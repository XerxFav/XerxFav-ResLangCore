class MemoryStore:
    def __init__(self):
        self._store = {}

    def save(self, key, value):
        self._store[key] = value
        print(f"[Memory] Saved: {key} → {value}")

    def load(self, key):
        value = self._store.get(key)
        print(f"[Memory] Loaded: {key} → {value}")
        return value

    def clear(self):
        self._store.clear()
        print("[Memory] Cleared")
