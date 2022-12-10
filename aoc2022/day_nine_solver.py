from dataclasses import dataclass
import re

from aoc2022.solver import Solver


@dataclass
class Point:
    x: int
    y: int

    def x_distance(self, other: "Point"):
        coords = self.x, other.x

        return max(*coords) - min(*coords)

    def y_distance(self, other: "Point"):
        coords = self.y, other.y

        return max(*coords) - min(*coords)

    def recalculate_other(self, other: "Point"):
        new = Point(other.x, other.y)

        x_distance = self.x_distance(other)
        y_distance = self.y_distance(other)

        # If they are touching
        if abs(x_distance) <= 1 and abs(y_distance) <= 1:
            return new

        # If they are two points or more directly up, left, down, right
        elif self.x == other.x or self.y == other.y:
            if self.x == other.x:
                if self.y + 1 > other.y:
                    new.y += 1
                else:
                    new.y -= 1
            elif self.y == other.y:
                if self.x + 1 > other.x:
                    new.x += 1
                else:
                    new.x -= 1

            return new

        # If they aren't touching and aren't in the same row or column
        else:
            if self.x > other.x:
                new.x += 1
            elif self.x < other.x:
                new.x -= 1
            
            if self.y > other.y:
                new.y += 1
            elif self.y < other.y:
                new.y -= 1

            return new

    def __hash__(self):
        return hash((self.x, self.y))


class DayNineSolver(Solver):
    def solve_part_one(self):
        head = Point(0, 0)
        tail = Point(0, 0)
        visited = set([tail])

        instruction_pattern = re.compile(r"([ULDR]) (\d+)")
        for line in self.data.split("\n"):
            direction, distance = instruction_pattern.match(line).groups()
            for _ in range(int(distance)):
                if direction == "U":
                    head = Point(head.x, head.y + 1)
                elif direction == "D":
                    head = Point(head.x, head.y - 1)
                elif direction == "L":
                    head = Point(head.x - 1, head.y)
                elif direction == "R":
                    head = Point(head.x + 1, head.y)
                tail = head.recalculate_other(tail)
                visited.add(tail)

        return len(visited)

    def solve_part_two(self):
        # 10 knots
        knots = [Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0),
                 Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0), Point(0, 0)]

        visited = set([knots[0]])

        instruction_pattern = re.compile(r"([ULDR]) (\d+)")
        for line in self.data.split("\n"):
            direction, distance = instruction_pattern.match(line).groups()
            for _ in range(int(distance)):
                head = knots[-1]
                if direction == "U":
                    head = Point(head.x, head.y + 1)
                elif direction == "D":
                    head = Point(head.x, head.y - 1)
                elif direction == "L":
                    head = Point(head.x - 1, head.y)
                elif direction == "R":
                    head = Point(head.x + 1, head.y)
                knots[-1] = head
                
                for i in range(len(knots) - 2, -1, -1):
                    knots[i] = head.recalculate_other(knots[i])
                    head = knots[i]
                visited.add(knots[0])

        return len(visited)
