import os
import numpy as np

DIRPATH = os.path.dirname(os.path.realpath(__file__))

class Solver:
    def __init__(self, file_name):
        self.file_name = file_name
        self.number_snakes = 0
        self.snakes_length = []
        self.board = None

        self.r = 0
        self.c = 0

        # LEGGI FILE
        with open(f"{DIRPATH}/data/{file_name}.txt", 'r') as f:
            file_content = f.read().split("\n")

            # read first line
            first_line = file_content[0].split(" ")
            self.c, self.r, self.number_snakes = [int(elem) for elem in first_line]

            self.board = []

            # read second line
            second_line = file_content[1].split(" ")
            self.snakes_length = [int(elem) for elem in second_line]

            # read board
            for i in range(2, 2 + self.r):
                row_tmp = file_content[i].strip().split()
                self.board.append(row_tmp)




        # convert strings in board into numbers
        for i in range(len(self.board)):
            self.board[i] = [int(e) if e != '*' else e for e in self.board[i]]
        print("input letto")
        print(self.board)

        self.calculate_score(f"./out/output.txt")





    def solve(self):
        pass




    def to_output(self):
       pass
       #with open(f"./out/{self.file_name}_out.txt", "w") as file:

    def calculate_score(self, output_file):
        score = 0
        wormhole = False  # brutto modo di gestire i wormhole
        x_max = self.c-1
        y_max = self.r-1
        input_matrix = self.board.copy()


        with open(output_file, "r") as output:
            for line in output.readlines():
                line = line.replace(" ", "")
                line = line.strip()
                x = int(line[0])
                y = int(line[1])
                score += input_matrix[y][x]
                # print(y_start, x_start)
                for char in line[2:]:
                    if char == "R":
                        if x == x_max:
                            x = 0
                        else:
                            x += 1
                    elif char == "L":
                        if x == 0:
                            x = x_max
                        else:
                            x -= 1
                    elif char == "D":
                        if y == y_max:
                            y = 0
                        else:
                            y += 1
                    elif char == "U":
                        if y == 0:
                            y = y_max
                        else:
                            y -= 1
                    else:
                        if not wormhole:
                            wormhole = True
                            x = int(char)
                        else:
                            wormhole = False
                            y = int(char)

                    if not wormhole:
                        if input_matrix[y][x] != '*':
                            score += int(input_matrix[y][x])

        print(score)
        return score



