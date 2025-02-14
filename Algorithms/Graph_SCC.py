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


class Tarjan:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.id = -1
        self.stack = []
        self.cur_scc = []
        self.sccs = []
        self.ids = graph.size() * [-1]
        self.lls = graph.size() * [0]
        self.onStack = graph.size() * [False]

    def tarjan(self):
        for v in self.graph.a_list:
            if self.ids[v.index] == -1:
                self.dfs(v)
        return self.sccs

    def dfs(self, vertex):
        self.id += 1
        self.stack.append(vertex)
        self.onStack[vertex.index] = True
        self.ids[vertex.index] = self.lls[vertex.index] = self.id

        for n in vertex.neighbors:
            if self.ids[n.index] == -1:
                self.dfs(n)
            if self.onStack[n.index]:
                self.lls[vertex.index] = min(self.lls[n.index], self.lls[vertex.index])

        if self.lls[vertex.index] == self.ids[vertex.index]:
            while self.stack:
                node = self.stack.pop()
                self.cur_scc.append(node)
                if node == vertex:
                    scc = self.cur_scc.copy()
                    self.sccs.append(scc)
                    self.cur_scc = []
                    break


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



    print('Kosaraju')
    kos = Kosaraju(g)
    print(kos.scc())

    new_graph = Graph()
    new_graph.addVertex(Vertex(0))
    new_graph.addVertex(Vertex(1))
    new_graph.addVertex(Vertex(2))
    new_graph.addVertex(Vertex(3))
    new_graph.addVertex(Vertex(4))
    new_graph.addVertex(Vertex(5))
    new_graph.addVertex(Vertex(6))

    new_graph.addEdge(0, 1)
    new_graph.addEdge(1, 6)
    new_graph.addEdge(1, 2)
    new_graph.addEdge(1, 4)
    new_graph.addEdge(2, 3)
    new_graph.addEdge(3, 2)
    new_graph.addEdge(3, 4)
    new_graph.addEdge(3, 5)
    new_graph.addEdge(4, 5)
    new_graph.addEdge(5, 4)
    new_graph.addEdge(6, 0)
    new_graph.addEdge(6, 2)


    print('Tarjan')
    tar = Tarjan(new_graph)
    print(tar.tarjan())
