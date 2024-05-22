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
        self.path = None

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

    def dfs(self, index=0):
        if self.__visited[index]:
            return
        self.__visited[index] = True
        # print(self.vertexes[index])
        for i in range(len(self.a_matrix)):
            if self.a_matrix[index][i] and not self.__visited[i]:
                self.dfs(i)
        print(self.vertexes[index])

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

    def countLevelNodes(self, level):
        if level == 0:
            print(f'Level {level}: ')
            return 1
        cur_level = 1
        self.q.clear()
        self.__visited = [False] * len(self.vertexes)
        self.q.append(self.vertexes[0])
        self.__visited[0] = True
        last = self.vertexes[0]
        completed = False
        while self.q:
            ver = self.q.popleft()
            if ver is last:
                completed = True
            for i in range(len(self.a_matrix)):
                if self.a_matrix[ver.index][i]:
                    if not self.__visited[i]:
                        self.q.append(self.vertexes[i])
                    self.__visited[i] = True
            if completed:
                last = self.q[-1]
                if cur_level == level:
                    print(f'Level {cur_level}: ')
                    return len(self.q)
                else:
                    completed = False
                    cur_level += 1

    def __dfsPath(self, src, dst, res):
        if self.__visited[src]:
            return
        res.append(self.vertexes[src])
        self.__visited[src] = True
        for i in range(len(self.a_matrix)):
            if self.a_matrix[src][i]:
                if not self.__visited[i]:
                    self.__dfsPath(i, dst, res)
        if src == dst:
            if not self.path or len(res) < len(self.path):
                self.path = res.copy()
        self.__visited[src] = False
        res.pop()
        return self.path

    def findShortestPath(self, source, destination):
        result = []
        return self.__dfsPath(source, destination, result)

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
    g.addVertex(Vertex(5))
    g.addVertex(Vertex(6))
    g.addVertex(Vertex(7))

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(1, 0)
    g.addEdge(1, 5)
    g.addEdge(1, 4)
    g.addEdge(2, 0)
    g.addEdge(2, 4)
    g.addEdge(3, 0)
    g.addEdge(3, 4)
    g.addEdge(3, 6)
    g.addEdge(4, 1)
    g.addEdge(4, 2)
    g.addEdge(4, 3)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 1)
    g.addEdge(5, 7)
    g.addEdge(6, 3)
    g.addEdge(6, 4)
    g.addEdge(7, 4)
    g.addEdge(7, 5)

    # for v in g.vertexes:
    #     print(v)
    # for row in g.a_matrix:
    #     print(row)
    # g.bfs()
    # g.dfs()
    # print(g.countLevelNodes(0))
    # print(g.countLevelNodes(1))
    # print(g.countLevelNodes(2))
    # print(g.countLevelNodes(3))
    print(g.findShortestPath(0, 6))
