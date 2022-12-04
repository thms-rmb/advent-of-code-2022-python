import importlib.resources

from aoc2022.day_four_solver import DayFourSolver
import aoc2022.inputs

solvers = [
    (4, DayFourSolver)
]

def main():
    print("Going to solve puzzles.")
    for day, solver_class in solvers:
        solver = solver_class(importlib.resources.read_text(aoc2022.inputs, day))
        print(f"Day {day}, part 1: {solver.solve_part_one()}")
        print(f"Day {day}, part 2: {solver.solve_part_two()}")


if __name__ == "__main__":
    main()
