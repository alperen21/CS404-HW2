from ortools.sat.python import cp_model

class Constraint:
    def __init__(self, x_coordinate, y_coordinate, value) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.value = value

class Board:
    def __init__(self) -> None:
        self.__model = cp_model.CpModel()

    def __createMatrix(self, size):
        """
        creates matrices

        :param size: size of the matrix
        """
        return [[self.__model.NewIntVar(0, 1, f"{i},{j}") for i in range(size)] for j in range(size)]

    def __filterInvalidCoordinates(self, coordinates : list) -> list:
        return list(filter(lambda coordinate: 
                coordinate[0] >= 0 and coordinate[1] >= 0 and
                coordinate[0] < self.__size-1 and coordinate[1] < self.__size-1,
                coordinates))
    
    def __getWatchCoordinatesLeft(self, constraint : Constraint):
        coordinates = [
            (constraint.x_coordinate, constraint.y_coordinate),
            (constraint.x_coordinate-1, constraint.y_coordinate-1),
        ]

        return self.__filterInvalidCoordinates(coordinates)

    def __getWatchCoordinatesRight(self, constraint : Constraint):
        coordinates = [
            (constraint.x_coordinate-1, constraint.y_coordinate),
            (constraint.x_coordinate, constraint.y_coordinate-1),
        ]

        return self.__filterInvalidCoordinates(coordinates)
    
    def __addConstraints(self) -> None:
        for constraint in self.__constraints:
            left_watch = self.__getWatchCoordinatesLeft(constraint)
            right_watch = self.__getWatchCoordinatesRight(constraint)

            boolean_expression = []

            for x,y in left_watch:
                boolean_expression.append(f"{f'{self.leftMatrix=}'.split('=')[0]}[{x}][{y}]")

            for x,y in right_watch:
                boolean_expression.append(f"{f'{self.rightMatrix=}'.split('=')[0]}[{x}][{y}]")

            boolean_expression = " + ".join(boolean_expression) + " == " + str(constraint.value)
            self.__model.Add(eval(boolean_expression))

        
        for x in range(self.__size-1):
            for y in range(self.__size-1):
                self.__model.Add(self.leftMatrix[x][y] != self.rightMatrix[x][y])

    def initialize(self, filename : str) -> None:
        """
        initializes the matrices and constraints

        :param filename: name of the file that contains the constraints
        """
        self.__constraints = list()
        self.__size = 0
        with open(filename, "r") as file:
            lines = file.readlines()
            self.__size = len(lines)

            for x_coordinate, line in enumerate(lines):
                elems = line.strip().split(" ")
                for y_coordinate, elem in enumerate(elems):
                    if elem != "*":
                        self.__constraints.append(Constraint(x_coordinate, y_coordinate, int(elem)))
        
        self.rightMatrix = self.__createMatrix(self.__size - 1)
        self.leftMatrix = self.__createMatrix(self.__size - 1)

        self.__addConstraints()
    
    def solve(self) -> None:
        """
        Solve the constraint satisfaction problem
        """
        self.__solver = cp_model.CpSolver()
        status = self.__solver.Solve(self.__model)

        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            print("left matrix")
            for row in self.leftMatrix:
                for elem in row:
                    print(elem, "->", self.__solver.Value(elem))

            print("right matrix")
            for row in self.rightMatrix:
                for elem in row:
                    print(elem, "->", self.__solver.Value(elem))
        else:
            print('No solution found.')


    
    


                


