from sympy.parsing.latex import parse_latex

class Step:
    pass

class ExpressionList:
    initial = {}
    guess = {}
    steps = []

    def __init__(self, obj):
        """Parse JSON objects into an expression list
        so that it can be used by others easier"""
        for step in obj:
            # Store each object as a sympy expression
            expr = parse_latex(step["expr"])

            step_type = step["type"]
            if step_type == "initial":
                self.initial = expr
            elif step_type == "step":
                self.steps.append(expr)
            elif step_type == "guess":
                self.guess = expr
