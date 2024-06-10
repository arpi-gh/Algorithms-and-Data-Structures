from Weighted_graph import Graph, Vertex
from queue import PriorityQueue
from math import inf


class Edge:
    def __init__(self, src: Vertex, dst: Vertex, cost: int or float):
        self.src = src
        self.dst = dst
        self.cost = cost

    def __eq__(self, other):
        if self.cost == other.cost:
            return True
        return False

    def __gt__(self, other):
        if self.cost > other.cost:
            return True
        return False

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        return False

    def __repr__(self):
        return f'{self.src}->{self.dst}<{self.cost}>'


class Prim:
    def __init__(self, graph: Graph):
        self.graph = graph

    def addEdge(self, minheap: PriorityQueue, vertex: Vertex):
        for i in range(len(self.graph.a_matrix)):
            if self.graph.a_matrix[vertex.index][i] != float(inf):
                e = Edge(vertex, self.graph.vertexes[i], self.graph.a_matrix[vertex.index][i])
                minheap.put(e)

    def lazyPrim(self):
        size = self.graph.getSize() - 1
        start = self.graph.vertexes[0]
        pq = PriorityQueue()
        visited = [False] * self.graph.getSize()
        visited[0] = True
        mst = [start]
        self.addEdge(pq, start)
        edges = []
        overall_cost = 0
        while pq and len(edges) != size:
            edge = pq.get()
            next = edge.dst
            if not visited[next.index]:
                visited[next.index] = True
                mst.append(next)
                edges.append(edge)
                overall_cost += edge.cost
                self.addEdge(pq, next)
        if len(mst) != self.graph.getSize():
            return None
        return overall_cost


if __name__ == '__main__':
    g = Graph()
    g.addVertex(Vertex(0))
    g.addVertex(Vertex(1))
    g.addVertex(Vertex(2))
    g.addVertex(Vertex(3))
    g.addVertex(Vertex(4))
    g.addVertex(Vertex(5))
    g.addVertex(Vertex(6))

    g.addEdge(0, 1, 9)
    g.addEdge(0, 2, 0)
    g.addEdge(0, 3, 5)
    g.addEdge(0, 5, 7)
    g.addEdge(1, 3, -2)
    g.addEdge(1, 4, 3)
    g.addEdge(1, 6, 4)
    g.addEdge(2, 5, 6)
    g.addEdge(3, 5, 2)
    g.addEdge(3, 6, 3)
    g.addEdge(4, 6, 6)
    g.addEdge(5, 6, 1)

    sol = Prim(g)
    print(sol.lazyPrim())











