from Board.Board import Board, Constraint
from cycle.Node import Graph
from pprint import pprint

def main():
    board = Board()
    board.initialize("input.txt")
    solution_matrix = board.solve()
    pprint(solution_matrix[0])
    # graph = Graph(6)
    # graph.initialize_children(solution_matrix) 
    # graph.print()


    

if __name__ == "__main__":
    main()