from aoc2022.solver import Solver

rock = 1
paper = 2
scissor = 3

opponent_mapping = dict(A=rock, B=paper, C=scissor)
opponent_mapping_reverse = {val: choice for choice, val in opponent_mapping.items()}
me_mapping = dict(X=rock, Y=paper, Z=scissor)
win_strats = {rock: scissor, scissor: paper, paper: rock}


class DayTwoSolver(Solver):
    def solve_part_one(self):
        score = 0
        for game in self.data.split("\n"):
            left, right = game.split(" ")
            score += me_mapping.get(right, 0)
            if win_strats[me_mapping[right]] == opponent_mapping[left]:
                score += 6
            elif win_strats[opponent_mapping[left]] == me_mapping[right]:
                pass
            else:
                score += 3

        return score

    def solve_part_two(self):
        score = 0
        for game in self.data.split("\n"):
             left, right = game.split(" ")
             if right == "X":
                 score += win_strats[opponent_mapping[left]]
             elif right == "Y":
                 score += opponent_mapping[left] + 3
             else:
                 for strat, beats in win_strats.items():
                     if opponent_mapping_reverse[beats] == left:
                         score += strat + 6

        return score
