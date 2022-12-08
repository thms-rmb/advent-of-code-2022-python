import importlib.resources

from aoc2022.day_one_solver import DayOneSolver
from aoc2022.day_two_solver import DayTwoSolver
from aoc2022.day_three_solver import DayThreeSolver
from aoc2022.day_four_solver import DayFourSolver
from aoc2022.day_five_solver import DayFiveSolver
from aoc2022.day_eight_solver import DayEightSolver
import aoc2022.inputs

solvers = [
    (1, DayOneSolver),
    (2, DayTwoSolver),
    (3, DayThreeSolver),
    (4, DayFourSolver),
    (5, DayFiveSolver),
    (8, DayEightSolver)
]

def main():
    print("Going to solve puzzles.")
    for day, solver_class in solvers:
        solver = solver_class(importlib.resources.read_text(aoc2022.inputs, day))
        print(f"Day {day}, part 1: {solver.solve_part_one()}")
        print(f"Day {day}, part 2: {solver.solve_part_two()}")


if __name__ == "__main__":
    main()
