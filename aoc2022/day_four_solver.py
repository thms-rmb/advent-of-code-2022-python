from aoc2022.solver import Solver

class DayFourSolver(Solver):
    def __init__(self, data):
        super().__init__(data)
        self._pairs = None

    @staticmethod
    def does_fully_contain(pair):
        for left, right in pair, reversed(pair):
            if left[0] <= right[0] and left[1] >= right[1]:
                return True
        return False

    def solve_part_one(self):
        return len([pair for pair in self.pairs if self.does_fully_contain(pair)])

    @staticmethod
    def does_partly_contain(pair):
        for (left_lower, left_upper), right_bounds in pair, reversed(pair):
            for right_bound in right_bounds:
                if left_lower <= right_bound and left_upper >= right_bound:
                    return True
        return False

    def solve_part_two(self):
        return len([pair for pair in self.pairs if self.does_partly_contain(pair)])

    @property
    def pairs(self):
        if self._pairs is None:
            self._pairs = []
            for line in self.data.split("\n"):
                sections = [[int(bound) for bound in section.split("-")] for section in line.split(",")]
                self._pairs.append(sections)

        return self._pairs
