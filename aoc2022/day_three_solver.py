from aoc2022.solver import Solver


class DayThreeSolver(Solver):
    @property
    def scores(self):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        return {char: i + 1 for i, char in enumerate(chars)}

    def solve_part_one(self):
        score = 0
        for contents in self.data.split("\n"):
            left, right = contents[:int(len(contents) / 2)], contents[int(len(contents) / 2):]
            common = (set(left) & set(right)).pop()
            score += self.scores[common]

        return score

    def solve_part_two(self):
        score = 0
        for i, contents in enumerate(self.data.split("\n")):
            remainder = (i + 4) % 3
            if remainder == 1:
                common = set(contents)
            elif remainder == 0:
                common &= set(contents)
                score += self.scores[common.pop()]
                common = set()
            else:
                common &= set(contents)

        return score
