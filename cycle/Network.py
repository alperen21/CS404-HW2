import networkx as nx


class Graph:    
    def initialize(self, slantMatrix : str) -> None:
        edgelist = list()

        for x_coordinate, line in enumerate(slantMatrix):
            for y_coordinate, elem in enumerate(line):
                if elem == 1:
                   # self.matrix[x_coordinate+1][y_coordinate].children.append(Coordinate(x_coordinate, y_coordinate+1))
                   edgelist.append(
                       (f"({x_coordinate+1},{y_coordinate})", f"({x_coordinate},{y_coordinate+1})")
                   )

                #    edgelist.append(
                #        (f"({x_coordinate},{y_coordinate+1})", f"({x_coordinate+1},{y_coordinate})")
                #        )
                if elem == -1:
                    edgelist.append(
                       (f"({x_coordinate},{y_coordinate})", f"({x_coordinate+1},{y_coordinate+1})")
                   )
                    # edgelist.append(
                    #     (f"({x_coordinate+1},{y_coordinate+1})", f"({x_coordinate},{y_coordinate})")
                    # )
        
        self.network = nx.Graph(edgelist)

        return edgelist
    
    def getCycle(self):
        for cycle in nx.simple_cycles(self.network):
            print(cycle)