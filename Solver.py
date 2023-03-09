import os
import numpy as np

DIRPATH = os.path.dirname(os.path.realpath(__file__))


class Snake:
    def __init__(self, ch, rh, length):
        self.ch = ch
        self.rh = rh
        self.len = length


class Solver:
    def __init__(self, file_name):
        self.file_name = file_name
        self.snakes = 0
        self.board = None

        self.r = 0
        self.c = 0

        # LEGGI FILE
        with open(f"{DIRPATH}/data/{file_name}.txt", 'r') as f:
            file_content = f.read().split("\n")

            # read first line
            first_line = file_content[0].split(" ")
            self.c, self.r, self.snakes = [int(elem) for elem in first_line]

            self.board = []

            # read second line
            second_line = file_content[1].split(" ")
            lenghts = [int(elem) for elem in second_line]

            # read board
            for i in range(2, 2 + self.snakes):
                row = file_content[i].strip().split()

                self.board.append(row)



        # convert strings in board into numbers
        for i in range(len(self.board)):
            self.board[i] = [int(e) if e is not '*' else e for e in row]
        print("input letto")
        print(self.board)






    def solve(self):
        pass




    def to_output(self):
        with open(f"./out/{self.file_name}_out.txt", "w") as file:
            pass