from arca_langlib.types.phase_types import PhaseSignature

sig = PhaseSignature("example", [("input1", "string")], [("result", "int")])
print("Phase Signature:")
print(sig.describe())
