from Board.Board import Board, Constraint
from cycle.Network import Graph
from pprint import pprint

def main():
    board = Board()
    board.initialize("input.txt")
    solution_matrix = board.solve()
    pprint(solution_matrix[10])


    graph = Graph()
    graph.initialize(solution_matrix[0])

    graph.getCycle()
    # graph.initialize_children(solution_matrix[10]) 
    # graph.print()




    

if __name__ == "__main__":
    main()