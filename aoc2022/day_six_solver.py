from aoc2022.solver import Solver

class DaySixSolver(Solver):
    def solve_part_one(self):
        for i in range(0, len(self.data)):
            if len(set(self.data[i:i+4])) == 4:
                return i+4

    def solve_part_two(self):
        for i in range(0, len(self.data)):
            if len(set(self.data[i:i+14])) == 14:
                return i+14
