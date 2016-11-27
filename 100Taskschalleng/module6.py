import math
class EquationSolver:
    def __init__(self, **kwargs):
        return super().__init__(**kwargs)
    def solve(self, valuesOfD):
        self.result = list()
        for v in valuesOfD.split(","):
            v = int(v)
            self.result.append(round(math.sqrt((100*v)/30)))
        print(self.result)
obj = EquationSolver()
obj.solve(input())