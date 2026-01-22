class ExpressionSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        result = (self.a + self.b) * self.c
        return result

calc = ExpressionSolver(10, 5, 2)
print("The result of (a + b) * c is:", calc.solve())