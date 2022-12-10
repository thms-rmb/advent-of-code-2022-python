import importlib.resources

from aoc2022.day_one_solver import DayOneSolver
from aoc2022.day_two_solver import DayTwoSolver
from aoc2022.day_three_solver import DayThreeSolver
from aoc2022.day_four_solver import DayFourSolver
from aoc2022.day_five_solver import DayFiveSolver
from aoc2022.day_six_solver import DaySixSolver
from aoc2022.day_seven_solver import DaySevenSolver
from aoc2022.day_nine_solver import DayNineSolver
import aoc2022.inputs

solvers = [
    (1, DayOneSolver),
    (2, DayTwoSolver),
    (3, DayThreeSolver),
    (4, DayFourSolver),
    (5, DayFiveSolver),
    (6, DaySixSolver),
    (7, DaySevenSolver),
    (9, DayNineSolver)
]

def main():
    print("Going to solve puzzles.")
    for day, solver_class in solvers:
        solver = solver_class(importlib.resources.read_text(aoc2022.inputs, day))
        print(f"Day {day}, part 1: {solver.solve_part_one()}")
        print(f"Day {day}, part 2: {solver.solve_part_two()}")


if __name__ == "__main__":
    main()
