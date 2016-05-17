

class Graph(object):

    def __init__(self, graph_dictionary=None):
        if graph_dictionary is None:
            graph_dictionary = {}
        self.__graph_dict = graph_dictionary

    def get_vertices(self):
        return self.__graph_dict.keys()

    def get_edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_egde(self, edge):
        if len(edge) != 2:
            return None
        edge = set(edge)
        (start_vertex, end_vertex) = tuple(edge)
        if start_vertex in self.__graph_dict:
            self.__graph_dict[start_vertex].append(end_vertex)
        else:
            self.__graph_dict[start_vertex] = [end_vertex]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res