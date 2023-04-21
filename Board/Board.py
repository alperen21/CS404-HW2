from ortools.sat.python import cp_model
from ortools.sat.python import swig_helper
from pprint import pprint 
import ortools

class Constraint:
    def __init__(self, x_coordinate, y_coordinate, value) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.value = value

class SolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__left_variables = list()
        self.__right_variables = list()
        
        self.left_solution_list = []
        self.right_solution_list = []

    def addLeftVariables(self, leftMatrix):
        for row in leftMatrix:
            for variable in row:
                self.__left_variables.append(variable)
    
    
    def addRightVariables(self, rightMatrix):
        for row in rightMatrix:
            for variable in row:
                self.__right_variables.append(variable)
    
    
    def on_solution_callback(self):
        self.left_solution_list.append([self.Value(v) for v in self.__left_variables])
        self.right_solution_list.append([self.Value(v) for v in self.__right_variables])


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
        """
        filters out invalid coordinates

        :param coordinates: coordinates to be filtered
        """
        return list(filter(lambda coordinate: 
                coordinate[0] >= 0 and coordinate[1] >= 0 and
                coordinate[0] < self.__size-1 and coordinate[1] < self.__size-1,
                coordinates))
    
    def __getWatchCoordinatesLeft(self, constraint : Constraint):
        """
        returns values that need to be watched in leftMatrix

        :param constraint: the constraint that will generate the coordinates
        """
        coordinates = [
            (constraint.x_coordinate, constraint.y_coordinate),
            (constraint.x_coordinate-1, constraint.y_coordinate-1),
        ]

        return self.__filterInvalidCoordinates(coordinates)

    def __getWatchCoordinatesRight(self, constraint : Constraint):
        """
        returns values that need to be watched in rightMatrix

        :param constraint: the constraint that will generate the coordinates
        """
        coordinates = [
            (constraint.x_coordinate-1, constraint.y_coordinate),
            (constraint.x_coordinate, constraint.y_coordinate-1),
        ]

        return self.__filterInvalidCoordinates(coordinates)
    
    def __addConstraints(self) -> None:
        """
        adds constraints to the model
        """
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

    def __literal_to_matrix(self, literal):
        matrix = list()
        for i in range(0, len(literal), self.__size-1):
            matrix.append(literal[i:i+self.__size-1])
        return matrix

    def solve(self) -> list:
        """
        Solve the constraint satisfaction problem
        """
        self.__solutionMatrix = [[0 for _ in range(self.__size - 1)] for _ in range(self.__size - 1)]
        self.__solver = cp_model.CpSolver()
        
        # self.__solver.parameters.num_search_workers = 8
        self.__solver.parameters.enumerate_all_solutions = True
        # self.__solver.AddSolutionCallback(SolutionPrinter)

        solutionCollector = SolutionCollector()
        solutionCollector.addLeftVariables(self.leftMatrix)
        solutionCollector.addRightVariables(self.rightMatrix)

        status = self.__solver.Solve(self.__model, solutionCollector)

        all_solutions = list()
        if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
            for left_solution, right_solution in zip(solutionCollector.left_solution_list, solutionCollector.right_solution_list):
                combined = list()

                for left_elem, right_elem in zip(left_solution, right_solution):
                    if left_elem == 1:
                        combined.append(-1)
                    elif right_elem == 1:
                        combined.append(1)
                
                all_solutions.append(self.__literal_to_matrix(combined))

        return all_solutions
    
    def getNumberOfBacktracks(self):
        return self.__solver.NumBooleans()

    def getNumberOfVariables(self):
        return len(self.leftMatrix) * len(self.leftMatrix[0]) + len(self.rightMatrix) * len(self.rightMatrix[0])
    
    def getNumberOfConstraints(self):
        return len(self.__constraints)
    
    


                


