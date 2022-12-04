from aoc2022.solver import Solver

class DayOneSolver(Solver):
    def get_caloric_carriages(self):
        return [sum(int(calory) for calory in carriage.split("\n")) for carriage in self.data.split("\n\n")]

    def solve_part_one(self):
        return max(self.get_caloric_carriages())

    def solve_part_two(self):
        return sum(sorted(self.get_caloric_carriages(), reverse=True)[:3])
