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
    g.addVertex(Vertex('A'))
    g.addVertex(Vertex('B'))
    g.addVertex(Vertex('C'))
    g.addVertex(Vertex('D'))
    g.addVertex(Vertex('E'))
    g.addVertex(Vertex('F'))
    g.addVertex(Vertex('G'))
    g.addVertex(Vertex('H'))
    g.addVertex(Vertex('I'))
    g.addVertex(Vertex('J'))

    g.addEdge(0, 1, 5)
    g.addEdge(0, 3, 9)
    g.addEdge(0, 4, 1)
    g.addEdge(1, 2, 4)
    g.addEdge(1, 3, 2)
    g.addEdge(2, 7, 4)
    g.addEdge(2, 8, 1)
    g.addEdge(2, 9, 8)
    g.addEdge(3, 4, 2)
    g.addEdge(3, 5, 5)
    g.addEdge(3, 6, 11)
    g.addEdge(3, 7, 2)
    g.addEdge(4, 5, 1)
    g.addEdge(5, 6, 7)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 4)
    g.addEdge(7, 8, 6)
    g.addEdge(8, 9, 0)

    sol = Prim(g)
    print(sol.lazyPrim())













