from Weighted_graph import Graph, Vertex
from math import inf


class Dijkstra:
    def __init__(self, graph: Graph):
        self.graph = graph

    def dijkstra(self, src: Vertex, dst: Vertex):
        sorted_graph = g.Kahn()
        start = sorted_graph.index(src)
        end = sorted_graph.index(dst)
        sorted_graph = sorted_graph[start:end+1]
        dist = len(sorted_graph) * [inf]
        dist[0] = 0
        for i in range(len(sorted_graph)-1):
            for j in range(i+1, len(sorted_graph)):
                d = dist[i] + self.graph.getweight(sorted_graph[i], sorted_graph[j])
                if d < dist[j]:
                    dist[j] = d
        return dist[-1]


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

    g.addEdge(0, 1, 3)
    g.addEdge(0, 2, 6)
    g.addEdge(1, 2, 4)
    g.addEdge(1, 3, 4)
    g.addEdge(1, 4, 11)
    g.addEdge(2, 3, 8)
    g.addEdge(2, 6, 11)
    g.addEdge(3, 4, -4)
    g.addEdge(3, 5, 5)
    g.addEdge(3, 6, 2)
    g.addEdge(4, 7, 9)
    g.addEdge(5, 7, 1)
    g.addEdge(6, 7, 2)

    sol = Dijkstra(g)
    source = g.vertexes[0]
    destination = g.vertexes[7]
    print(sol.dijkstra(source, destination))






