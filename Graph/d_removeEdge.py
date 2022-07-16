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

    def add_edge(self, v1, v2): # vertex 1 and vertex 2 are arguments
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)  # v1 and v2 are now a key value pair
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError: # edge case where vertices are not connected
                pass
            return True
        return False

my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')


my_graph.add_edge('A','B')
my_graph.add_edge('B','C')
my_graph.add_edge('C','A')

my_graph.remove_edge('A','B')
my_graph.remove_edge('A','D')  # this edge does not exist- testing

my_graph.print_graph()


        
