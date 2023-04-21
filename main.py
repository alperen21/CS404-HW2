from Board.Board import Board
from cycle.Node import Graph

def main():
    board = Board()
    board.initialize("input.txt")
    solution_matrix = board.solve()
    graph = Graph(6)
    graph.initialize_children(solution_matrix) 
    graph.print()

    

if __name__ == "__main__":
    main()