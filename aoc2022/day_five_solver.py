from operator import itemgetter
import re

from aoc2022.solver import Solver


class DayFiveSolver(Solver):
    def __init__(self, data):
        super().__init__(data)
        self._procedures = None
        self.crate_layout, self.procedure_data = self.data.split("\n\n")

    def stacks(self):
        stacks = [[], [], [], [], [], [], [], [], []]

        pattern = re.compile(r"\[(\w)\]")
        for row in self.crate_layout.split("\n"):
            for stack_number, i in enumerate(range(0, len(row), 4)):
                crate = pattern.match(row[i:i+3])
                if crate is not None:
                    stacks[stack_number].insert(0, crate[1])

        return stacks

    @property
    def procedures(self):
        if self._procedures is None:
            self._procedures = []

            pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")
            for row in self.procedure_data.split("\n"):
                procedure = pattern.match(row)
                if procedure is None:
                    continue

                self._procedures.append([int(e) for e in procedure.groups()])

        return self._procedures

    def solve_part_one(self):
        stacks = self.stacks()
        for amount, source, target in self.procedures:
            for _ in range(amount):
                stacks[target - 1].append(stacks[source - 1].pop())

        return "".join(stack[-1] for stack in stacks if stack)

    def solve_part_two(self):
        stacks = self.stacks()
        for amount, source, target in self.procedures:
            carriage = []
            for _ in range(amount):
                carriage.insert(0, stacks[source - 1].pop())
            stacks[target - 1].extend(carriage)

        return "".join(stack[-1] for stack in stacks if stack)
