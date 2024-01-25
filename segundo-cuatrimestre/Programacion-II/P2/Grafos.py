# Grafos

# Grafos dirigidos
'''
Teniendo G=(V,E)
V={S,A,B,C,D,E,F,G,I,X}
E={{S,A}, {S,B},{S,C},{S,D},{C,F},{C,I},{A,G},{A,B},{D,C},{F,I},{D,E},{Z,X}}
'''

# Usando un diccionario G = {'S':['A','B','C', 'D']}

class DirectedGraph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex: int) -> int:
        if vertex in self.graph_dict:
            return('vertex in graph')
        self.graph_dict[vertex] = []

    def add_edge(self, edge: int):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)

    def is_vertex_in(self, vertex: int) -> bool:
        return vertex in self.graph_dict

    def get_vertex(self, vertex_name):
        for v in self.graph_dict:
            if vertex_name == v.get_name():
                return v
        print(f'vertex {vertex_name} doesnt exist')

    def get_neighbours(self, vertex) -> dict:
        return self.graph_dict[vertex]

    def __str__(self):
        all_edges=''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                all_edges += v1.get_name() + '--->' + v2.get_name() + '\n'
        return all_edges

class UndirectedGraph(DirectedGraph):
    def add_edge(self, edge):
        DirectedGraph.add_edge(self, edge)
        edge_back = Edge(edge.get_v2(),(edge.get_v1()))
        DirectedGraph.add_edge(self,edge_back)


class Edge:
    def __init__(self, v1: int,v2: int) -> None:
        self.v1=v1
        self.v2=v2

    def get_v1(self):
        return self.v1

    def get_v2(self):
        return self.v2

    def __str__(self):
        return (self.v1.get_name() + ' ----> ' + self.v2.get_name())

class Vertex:
    def __init__(self, name):
        self.name=name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name



def build_graph(graph):
    g=graph()
    for v in ('S','A','B','C','D','E','F','G','I','X'):
        g.add_vertex(Vertex(v))
    g.add_edge(Edge(g.get_vertex('S'), g.get_vertex('A')))
    g.add_edge(Edge(g.get_vertex('S'), g.get_vertex('B')))
    g.add_edge(Edge(g.get_vertex('S'), g.get_vertex('C')))
    g.add_edge(Edge(g.get_vertex('S'), g.get_vertex('D')))
    g.add_edge(Edge(g.get_vertex('C'), g.get_vertex('F')))
    g.add_edge(Edge(g.get_vertex('D'), g.get_vertex('E')))
    g.add_edge(Edge(g.get_vertex('B'), g.get_vertex('A')))


    return g

G1=build_graph(DirectedGraph)
print('Grafo dirigido:')
print(G1)
G2=build_graph(UndirectedGraph)
print('Grafo No dirigido:')
print(G2)