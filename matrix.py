
def createMatrix(filename : str, model):
    size = 0
    with open(filename, "r") as file:
        size = len(file.readlines()) - 1
    
    return [[model.NewIntVar(0, 1, f"{i},{j}") for i in range(size)] for j in range(size)]
