import re

from aoc2022.solver import Solver


class DayTenSolver(Solver):
    def solve_part_one(self):
        register = 1
        cycle = 0
        signal_strengths = []
        markers = 20, 60, 100, 140, 180, 220

        noop_pattern = re.compile("noop")
        addx_pattern = re.compile(r"addx (-?\d+)")

        for line in self.data.split("\n"):
            noop_match = noop_pattern.match(line)
            addx_match = addx_pattern.match(line)
            if noop_match is not None:
                for cycle in range(cycle + 1, cycle + 2):
                    if cycle in markers:
                        signal_strengths.append(cycle * register)

            elif addx_match is not None:
                x = int(addx_match[1])
                for cycle in range(cycle + 1, cycle + 3):
                    if cycle in markers:
                        signal_strengths.append(cycle * register)

                register += x

        return sum(signal_strengths)

    def solve_part_two(self):
        register = 1
        cycle = 0

        vertical = 0
        message = "\n"

        noop_pattern = re.compile("noop")
        addx_pattern = re.compile(r"addx (-?\d+)")

        def draw(vertical, message):
            if cycle - 1 - (40 * vertical) in (register - 1, register, register + 1):
                message += "#"
            else:
                message += "."

            if cycle % 40 == 0:
                message += "\n"
                vertical += 1

            return vertical, message

        for line in self.data.split("\n"):
            noop_match = noop_pattern.match(line)
            addx_match = addx_pattern.match(line)
            if noop_match is not None:
                for cycle in range(cycle + 1, cycle + 2):
                    vertical, message = draw(vertical, message)

            elif addx_match is not None:
                x = int(addx_match[1])
                for cycle in range(cycle + 1, cycle + 3):
                    vertical, message = draw(vertical, message)

                register += x

        return message
