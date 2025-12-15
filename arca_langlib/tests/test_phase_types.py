from arca_langlib.types.phase_types import PhaseSignature

def test_signature():
    sig = PhaseSignature("example", [("input1", "string")], [("result", "int")])
    print(sig.describe())

if __name__ == "__main__":
    test_signature()
