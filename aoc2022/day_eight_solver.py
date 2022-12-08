from functools import reduce

from aoc2022.solver import Solver

class DayEightSolver(Solver):
    def __init__(self, data):
        super().__init__(data)
        self.grid = [list(row) for row in self.data.split("\n")]

    def solve_part_one(self):
        x_bound = len(self.grid[0])
        y_bound = len(self.grid)

        visible = ((x_bound - 2) * 2) + ((y_bound - 2) * 2) + 4

        for i, row in enumerate(self.grid):
            if i == 0 or i + 1 == y_bound:
                continue

            for j, column in enumerate(row):
                if j == 0 or j + 1 == x_bound:
                    continue

                increment = False

                for y in range(i - 1, -1, -1):
                    if self.grid[y][j] >= column:
                        break
                else:
                    increment = True

                for x in range(j + 1, x_bound):
                    if self.grid[i][x] >= column:
                        break
                else:
                    increment = True

                for y in range(i + 1, y_bound):
                    if self.grid[y][j] >= column:
                        break
                else:
                    increment = True

                for x in range(j - 1, -1, -1):
                    if self.grid[i][x] >= column:
                        break
                else:
                    increment = True

                visible += increment

        return visible

    def solve_part_two(self):
        x_bound = len(self.grid[0])
        y_bound = len(self.grid)

        highest_scenic_score = 0
        for i, row in enumerate(self.grid):
            for j, column in enumerate(row):
                scenic_score = [0, 0, 0, 0]

                for y_up in range(i - 1, -1, -1):
                    scenic_score[0:1] = [scenic_score[0] + 1]
                    if self.grid[y_up][j] >= column:
                        break

                for x_right in range(j + 1, x_bound):
                    scenic_score[1:2] = [scenic_score[1] + 1]
                    if self.grid[i][x_right] >= column:
                        break

                for y_down in range(i + 1, y_bound):
                    scenic_score[2:3] = [scenic_score[2] + 1]
                    if self.grid[y_down][j] >= column:
                        break

                for x_right in range(j - 1, -1, -1):
                    scenic_score[3:4] = [scenic_score[3] + 1]
                    if self.grid[i][x_right] >= column:
                        break

                highest_scenic_score = max(highest_scenic_score, reduce(lambda left, right: left * right, scenic_score))

        return highest_scenic_score
