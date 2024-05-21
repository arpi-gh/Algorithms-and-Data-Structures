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
        self.a_list = []
        self.__visited = []
        self.q = deque()
        self.i = 0

    def addVertex(self, vertex: Vertex):
        self.a_list.append(vertex)
        vertex.index = self.i
        self.i += 1
        print(vertex.index)
        self.__visited.append(False)

    def addEdge(self, src: int, dst: int):
        if self.a_list[dst] not in self.a_list[src].neighbors:
            self.a_list[src].neighbors.append(self.a_list[dst])

    def checkEdge(self, src: int, dst: int):
        if self.a_list[dst] in self.a_list[src].neighbors or self.a_list[src] in self.a_list[dst].neighbors:
            return True
        return False

    def dfs(self, index=0):
        if self.__visited[index]:
            return
        self.__visited[index] = True
        print(self.a_list[index])
        for n in self.a_list[index].neighbors:
            if not self.__visited[n.index]:
                self.dfs(n.index)
        # print(self.a_list[index])

    def bfs(self):
        self.q.append(self.a_list[0])
        self.__visited[0] = True
        while self.q:
            ver = self.q.popleft()
            print(ver)
            for n in ver.neighbors:
                if not self.__visited[n.index]:
                    self.q.append(n)
                    self.__visited[n.index] = True

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
    # g.bfs()
    g.dfs()



