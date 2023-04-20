from ortools.sat.python import cp_model

model = cp_model.CpModel()

rightSlantGrid = [
    [model.NewIntVar(0, 1, "0,0"), model.NewIntVar(0, 1, "0,1"), model.NewIntVar(0, 1, "0,2")],
    [model.NewIntVar(0, 1, "1,0"), model.NewIntVar(0, 1, "1,1"), model.NewIntVar(0, 1, "1,2")],
    [model.NewIntVar(0, 1, "2,0"), model.NewIntVar(0, 1, "2,1"), model.NewIntVar(0, 1, "2,2")]

]

leftSlantGrid = [
    [model.NewIntVar(0, 1, "0,0"), model.NewIntVar(0, 1, "0,1"), model.NewIntVar(0, 1, "0,2")],
    [model.NewIntVar(0, 1, "1,0"), model.NewIntVar(0, 1, "1,1"), model.NewIntVar(0, 1, "1,2")],
    [model.NewIntVar(0, 1, "2,0"), model.NewIntVar(0, 1, "2,1"), model.NewIntVar(0, 1, "2,2")]
]

# X X X
# X X X
# X X X

model.Add(rightSlantGrid[0][0] + rightSlantGrid[1][1] + leftSlantGrid[0][1] + leftSlantGrid[1][0] == 4)
solver = cp_model.CpSolver()


status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("0,0", solver.Value(rightSlantGrid[0][0]))
    print("0,1", solver.Value(rightSlantGrid[0][1]))
    print("0,2", solver.Value(rightSlantGrid[0][2]))
    print("1,0", solver.Value(rightSlantGrid[1][0]))
    print("1,1", solver.Value(rightSlantGrid[1][1]))
    print("1,2", solver.Value(rightSlantGrid[1][2]))
    print("2,0", solver.Value(rightSlantGrid[2][0]))
    print("2,1", solver.Value(rightSlantGrid[2][1]))
    print("2,2", solver.Value(rightSlantGrid[2][2]))

    print("*******")

    print("0,0", solver.Value(leftSlantGrid[0][0]))
    print("0,1", solver.Value(leftSlantGrid[0][1]))
    print("0,2", solver.Value(leftSlantGrid[0][2]))
    print("1,0", solver.Value(leftSlantGrid[1][0]))
    print("1,1", solver.Value(leftSlantGrid[1][1]))
    print("1,2", solver.Value(leftSlantGrid[1][2]))
    print("2,0", solver.Value(leftSlantGrid[2][0]))
    print("2,1", solver.Value(leftSlantGrid[2][1]))
    print("2,2", solver.Value(leftSlantGrid[2][2]))

    
else:
    print('No solution found.')
