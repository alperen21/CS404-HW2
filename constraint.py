from ortools.sat.python import cp_model

def getWatchCoordinatesLeft(x_coordinate, y_coordinate, size): #\
    coordinates = [
        (x_coordinate, y_coordinate),
        # (x_coordinate-1, y_coordinate),
        # (x_coordinate, y_coordinate-1),
        (x_coordinate-1, y_coordinate-1),
    ]

    return list(filter(lambda coordinate: 
                    coordinate[0] >= 0 and coordinate[1] >= 0 and
                    coordinate[0] < size-1 and coordinate[1] < size-1,
                    coordinates))

def getWatchCoordinatesRight(x_coordinate, y_coordinate, size): #/
    coordinates = [
        # (x_coordinate, y_coordinate),
        (x_coordinate-1, y_coordinate),
        (x_coordinate, y_coordinate-1),
        # (x_coordinate-1, y_coordinate-1),
    ]

    return list(filter(lambda coordinate: 
                       coordinate[0] >= 0 and coordinate[1] >= 0 and
                       coordinate[0] < size-1 and coordinate[1] < size-1,
                       coordinates))



def getConstraintCoordinates(filename : str):
    constraints = list()

    with open(filename, "r") as file:
        for x, row in enumerate(file.readlines()):
            row = row.strip().split(" ")
            for y, elem in enumerate(row):
                if elem != "*":
                    constraints.append((x,y,int(elem)))
    
    return constraints

