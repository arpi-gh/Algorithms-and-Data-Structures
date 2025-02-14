from Directed_graph import Graph, Vertex
from collections import deque


class TopSort:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.n = graph.size()
        self.res = []
        self.visited = []

    def dfs(self, i):
        if self.visited[i]:
            return
        self.visited[i] = True
        for neighbor in self.graph.a_list[i].neighbors:
            self.dfs(neighbor.index)
        self.res[self.n] = self.graph.a_list[i]
        self.n -= 1

    def topsort(self):
        self.visited = [False] * self.n
        self.res = [0] * self.n
        self.n -= 1
        if not self.graph.hasCycle():
            for vertex in self.graph.a_list:
                if not self.visited[vertex.index]:
                    self.dfs(vertex.index)
            return self.res
        return None

    def enqueue(self, queue, edges_list):
        for i in range(len(edges_list)):
            if edges_list[i] == 0:
                queue.append(self.graph.a_list[i])
                edges_list[i] -= 1

    def Kahn(self):
        q = deque()
        edges = self.graph.size() * [0]
        res = []
        for vertex in self.graph.a_list:
            for neighbor in vertex.neighbors:
                edges[neighbor.index] += 1
        self.enqueue(q, edges)
        while q:
            v = q.popleft()
            res.append(v)
            for n in v.neighbors:
                edges[n.index] -= 1
            self.enqueue(q, edges)
        return res


if __name__ == '__main__':
    g = Graph()
    g.addVertex(Vertex(0))
    g.addVertex(Vertex(1))
    g.addVertex(Vertex(2))
    g.addVertex(Vertex(3))
    g.addVertex(Vertex(4))
    g.addVertex(Vertex(5))
    g.addVertex(Vertex(6))
    g.addVertex(Vertex(7))
    g.addVertex(Vertex(8))
    g.addVertex(Vertex(9))

    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 4)
    g.addEdge(3, 5)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 6)
    g.addEdge(5, 8)
    g.addEdge(6, 8)
    g.addEdge(6, 9)
    g.addEdge(7, 9)

    sol = TopSort(g)
    print(sol.topsort())
    print(sol.Kahn())





