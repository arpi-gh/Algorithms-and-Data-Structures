from collections import deque


class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.index = 0

    def __repr__(self):
        return f'{self.data}'


class Graph:
    def __init__(self):
        self.vertexes = []
        self.a_matrix = []
        self.__visited = []
        self.q = deque()
        self.i = 0

    def getSize(self):
        return len(self.a_matrix)

    def addVertex(self, vertex: Vertex):
        size = self.getSize()
        self.a_matrix.append([False] * size)
        for row in self.a_matrix:
            row.append(False)
        self.vertexes.append(vertex)
        vertex.index = self.i
        self.i += 1
        self.__visited.append(False)

    def addEdge(self, src: int, dst: int):
        self.a_matrix[src][dst] = True
        self.a_matrix[dst][src] = True   # In case it's an undirected graph

    def checkEdge(self, src: int, dst: int):
        if self.a_matrix[src][dst] is True:
            return True
        return False

    def dfs(self):
        ...

    def bfs(self):
        self.q.append(self.vertexes[0])
        self.__visited[0] = True
        while self.q:
            ver = self.q.popleft()
            print(ver)
            for i in range(len(self.a_matrix)):
                if self.a_matrix[ver.index][i]:
                    if not self.__visited[i]:
                        self.q.append(self.vertexes[i])
                        self.__visited[i] = True

    def countLevelNodes(self):
        ...

    def findShortestPath(self):
        ...

    def transpose(self):
        ...

    def __repr__(self):
        return f'{self.a_matrix}'


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

    for v in g.vertexes:
        print(v)
    for row in g.a_matrix:
        print(row)
    g.bfs()
