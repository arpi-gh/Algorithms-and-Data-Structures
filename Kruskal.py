from Weighted_graph import Graph, Vertex


class Kruskal:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.sizes = [1] * self.graph.getSize()
        self.reps = [i for i in range(self.graph.getSize())]
        self.edges = self.graph.edges.copy()
        self.result = 0

    def Kruskal(self):
        self.edges.sort(reverse=True)
        while self.edges:
            smallest = self.edges.pop()
            source = smallest.src
            destination = smallest.dst
            weight = smallest.cost
            if self.union(source.index, destination.index):
                self.result += weight
        return self.result

    def union(self, x, y) -> bool:
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.sizes[rootx] >= self.sizes[rooty]:
                self.sizes[rootx] += self.sizes[rooty]
                self.reps[rooty] = rootx
            else:
                self.sizes[rooty] += self.sizes[rootx]
                self.reps[rootx] = rooty
            return True

        else:
            return False

    def find(self, i):
        if self.reps[i] != i:
            return self.find(self.reps[i])
        else:
            return i


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
    g.addEdge(4, 5,1)
    g.addEdge(5, 6, 7)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 4)
    g.addEdge(7, 8, 6)
    g.addEdge(8, 9, 0)





    # print(len(g.edges))
    sol = Kruskal(g)
    print(sol.Kruskal())




