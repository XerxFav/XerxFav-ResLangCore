"""
Morphologic Space (F, O)
"""

class MorphologicSpace:
    def __init__(self, forms, operators):
        self.forms = forms
        self.operators = operators

    def equivalent(self, X, Y, invariant_fn):
        return invariant_fn(X) == invariant_fn(Y)
