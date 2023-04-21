import networkx as nx


class Graph:    
    def initialize(self, slantMatrix : str) -> None:
        edgelist = list()

        for x_coordinate, line in enumerate(slantMatrix):
            for y_coordinate, elem in enumerate(line):
                if elem == 1:
                   edgelist.append(
                       (f"({x_coordinate+1},{y_coordinate})", f"({x_coordinate},{y_coordinate+1})")
                   )

                if elem == -1:
                    edgelist.append(
                       (f"({x_coordinate},{y_coordinate})", f"({x_coordinate+1},{y_coordinate+1})")
                   )

        self.network = nx.Graph(edgelist)

        return edgelist
    
    def isCyclic(self):
        return len(list(nx.simple_cycles(self.network))) > 0