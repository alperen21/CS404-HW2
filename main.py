from Board.Board import Board, Constraint
from cycle.Network import Graph
from pprint import pprint
import sys

def getAcylicSolution(solutions):
    for solution in solutions:
        graph = Graph()
        graph.initialize(solution)

        if not graph.isCyclic():
            return solution

def translate(solution):
    for x in range(len(solution)):
        for y in range(len(solution)):
            if solution[x][y] == 1:
                solution[x][y] = "/"
            elif solution[x][y] == -1:
                solution[x][y] = "\\"
    
    return solution

def main():
    board = Board()
    board.initialize(f"./inputs/{sys.argv[1]}.txt")
    solution_matrix = board.solve()

    pprint(translate(getAcylicSolution(solution_matrix)))
    print(board.getNumberOfBacktracks())




    

if __name__ == "__main__":
    main()