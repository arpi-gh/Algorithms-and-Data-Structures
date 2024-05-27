from Directed_graph import Graph, Vertex


class Kosaraju:
    def __init__(self, graph: Graph):
        self.visited = []
        self.__scc = []
        self.graph = graph

    def scc(self):
        seen = self.graph.size() * [False]
        stack = []
        self.dfs(self.graph.a_list[0], stack, seen)
        self.graph.transpose()
        seen = self.graph.size() * [False]
        for v in stack[::-1]:
            if not seen[v.index]:
                tmp = []
                self.dfs(v, tmp, seen)
                self.__scc.append(tmp)
        return self.__scc

    def dfs(self, vertex: Vertex, ls: list, seen_vertices):
        if seen_vertices[vertex.index]:
            return
        seen_vertices[vertex.index] = True
        for neighbor in vertex.neighbors:
            self.dfs(neighbor, ls, seen_vertices)
        ls.append(vertex)
        return ls


if __name__ == '__main__':
    g = Graph()
    g.addVertex(Vertex(0))
    g.addVertex(Vertex(1))
    g.addVertex(Vertex(2))
    g.addVertex(Vertex(3))
    g.addVertex(Vertex(4))
    g.addVertex(Vertex(5))
    g.addVertex(Vertex(6))

    g.addEdge(0, 1)
    g.addEdge(1, 6)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 2)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 5)
    g.addEdge(5, 4)
    g.addEdge(6, 0)
    g.addEdge(6, 2)

    sol = Kosaraju(g)
    print(sol.scc())

