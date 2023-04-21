from pprint import pprint
from Board.Board import Board

class Coordinate:
    def __init__(self, x_coordinate, y_coordinate) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def __repr__(self) -> str:
        return f"({self.x_coordinate},{self.y_coordinate})"

class Node:
    def __init__(self, coordinate : Coordinate) -> None:
        self.coordinate = coordinate
        self.children = list()
    
    def __repr__(self) -> str:
        return str(self.children)
    
class Graph:
    def __init__(self, size) -> None:
        self.matrix = [[None for _ in range(size)] for _ in range(size)]

        for x_coordinate in range(size):
            for y_coordinate in range(size):
                coordinate = Coordinate(x_coordinate, y_coordinate)
                node = Node(coordinate)
                self.matrix[x_coordinate][y_coordinate] = node
    
    def initialize_children(self, slantMatrix : str) -> None:
        for x_coordinate, line in enumerate(slantMatrix):
            for y_coordinate, elem in enumerate(line):
                if elem == 1: # which means it is / bind (x+1, y) and (x,y+1)
                    self.matrix[x_coordinate+1][y_coordinate].children.append(Coordinate(x_coordinate, y_coordinate+1))
                    self.matrix[x_coordinate][y_coordinate+1].children.append(Coordinate(x_coordinate+1, y_coordinate))
                elif elem == -1: #which means it is \ bind (x,y) and (x+1, y+1)
                    self.matrix[x_coordinate][y_coordinate].children.append(Coordinate(x_coordinate+1, y_coordinate+1))
                    self.matrix[x_coordinate+1][y_coordinate+1].children.append(Coordinate(x_coordinate, y_coordinate))


    def print(self) -> None:
        for row in self.matrix:
            for elem in row:
                print(elem.coordinate ,elem.children)

    



