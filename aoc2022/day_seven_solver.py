import re

from aoc2022.solver import Solver

class DaySevenSolver(Solver):
    def obtain_tree(self):
        change_directory_command = re.compile(r"\$ cd (.+)")
        list_command = re.compile(r"\$ ls")
        directory_list_element = re.compile(r"dir (.+)")
        file_list_element = re.compile(r"(\d+) (.+)")

        tree = dict(children=dict(), type="dir", size=0)
        cursor = tree

        for line in self.data.split("\n")[1:]:
            if change_directory_command_match := change_directory_command.match(line):
                target = change_directory_command_match[1]
                if target == "..":
                    cursor = cursor.get("parent", cursor)
                else:
                    cursor = cursor["children"].setdefault(
                        target,
                        dict(
                            children=dict(),
                            type="dir",
                            size=0,
                            parent=cursor
                        )
                    )
            elif list_command_match := list_command.match(line):
                pass  # TODO: Act on list command
            elif directory_list_element_match := directory_list_element.match(line):
                target = directory_list_element_match[1]
                cursor["children"].setdefault(
                    target,
                    dict(
                        children=dict(),
                        type="dir",
                        size=0,
                        parent=cursor
                    )
                )
            elif file_list_element_match := file_list_element.match(line):
                size, name = file_list_element_match.groups()
                f = cursor["children"].setdefault(
                    name,
                    dict(
                        children=dict(),
                        type="file",
                        size=int(size),
                        parent=cursor
                    )
                )
                tmp_cursor = f
                while (tmp_cursor := tmp_cursor.get("parent")) is not None:
                    tmp_cursor["size"] += int(size)

        return tree

    def solve_part_one(self):
        def helper(cursor):
            if cursor["type"] == "file":
                return 0
            elif cursor["type"] == "dir":
                if cursor["size"] <= 100000:
                    return cursor["size"] + sum(helper(e) for e in cursor["children"].values())
                return sum(helper(e) for e in cursor["children"].values())
        
        return helper(self.obtain_tree())

    def solve_part_two(self):
        tree = self.obtain_tree()
        target = 30000000 - (70000000 - tree["size"])

        def get_sizes(cursor):
            if cursor["type"] == "file":
                return set()
            elif cursor["type"] == "dir":
                res = {cursor["size"]}
                for child in cursor["children"].values():
                    res |= get_sizes(child)
                return res

        sizes = get_sizes(tree)
        for size in sorted(sizes):
            if size >= target:
                return size
