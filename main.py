import sys

from Solver import Solver

if __name__ == '__main__':
    file_name = sys.argv[1]
    print(f"Solving file {file_name}...")
    problem = Solver(file_name)

    #problem.solve()
    #problem.to_output()

