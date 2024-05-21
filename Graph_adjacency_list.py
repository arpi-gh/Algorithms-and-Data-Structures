class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def __repr__(self):
        return f'{self.data}'


class Graph:
    def __init__(self):
        self.a_list = []
        self.__visited = [False] * len(self.a_list)

    def addVertex(self, vertex: Vertex):
        self.a_list.append(vertex)

    def addEdge(self, src: int, dst: int):
        if self.a_list[dst] not in self.a_list[src].neighbors:
            self.a_list[src].neighbors.append(self.a_list[dst])

    def checkEdge(self, src: int, dst: int):
        if self.a_list[dst] in self.a_list[src].neighbors or self.a_list[src] in self.a_list[dst].neighbors:
            return True
        return False

    def dfs(self):
        ...

    def bfs(self):
        ...

    def countLevelNodes(self):
        ...

    def findShortestPath(self):
        ...

    def transpose(self):
        ...

    def __repr__(self):
        return f'{self.a_list}'


if __name__ == '__main__':
    g = Graph()
    g.addVertex(Vertex(0))
    g.addVertex(Vertex(1))
    g.addVertex(Vertex(2))
    g.addVertex(Vertex(3))
    g.addVertex(Vertex(4))

    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 0)
    g.addEdge(2, 4)
    g.addEdge(3, 0)
    g.addEdge(3, 1)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(4, 2)

    for v in g.a_list:
        print(v, v.neighbors)



