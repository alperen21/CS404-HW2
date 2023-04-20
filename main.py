from constraint import getWatchCoordinatesLeft, getWatchCoordinatesRight, getConstraintCoordinates
import matrix
from ortools.sat.python import cp_model
from pprint import pprint


def getSize(fileName):
    with open(fileName, "r") as file:
        return len(file.readlines())

model = cp_model.CpModel()

constraints = getConstraintCoordinates("input.txt")

size = getSize("input.txt")

leftMatrix = matrix.createMatrix("input.txt", model)
rightMatrix = matrix.createMatrix("input.txt", model)


for constraint in constraints:
    left_watch = getWatchCoordinatesLeft(constraint[0], constraint[1], size)
    right_watch = getWatchCoordinatesRight(constraint[0], constraint[1], size)

    boolean_expression = []
    for x,y in left_watch:
        boolean_expression.append(f"leftMatrix[{x}][{y}]")
    
    for x,y in right_watch:
        boolean_expression.append(f"rightMatrix[{x}][{y}]")
    
    boolean_expression = " + ".join(boolean_expression) + " == " + str(constraint[2])

    model.Add(eval(boolean_expression))

for x in range(size-1):
    for y in range(size-1):
        model.Add(leftMatrix[x][y] != rightMatrix[x][y])

solver = cp_model.CpSolver()
status = solver.Solve(model)


print("left matrix")
for row in leftMatrix:
    for elem in row:
        print(elem, "->", solver.Value(elem))

print("right matrix")
for row in rightMatrix:
    for elem in row:
        print(elem, "->", solver.Value(elem))