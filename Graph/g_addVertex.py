class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():  # vertex should be unique and not added previously
            self.adj_list[vertex] = []  # setting = is actually : in dict, key-value pair
            return True                         
        return False

my_graph = Graph()

my_graph.add_vertex('A')

my_graph.print_graph()