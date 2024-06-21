from collections import deque
from math import inf


class Vertex:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.index = 0

    def __repr__(self):
        return f'{self.data}'


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


class Graph:
    def __init__(self):
        self.vertexes = []
        self.a_matrix = []
        self.__visited = []
        self.q = deque()
        self.i = 0
        self.cost = []
        self.path = None
        self.final_result = float(inf)
        self.weights = 0
        self.edges = []

    def getweight(self, src: Vertex, dst: Vertex):
        return self.a_matrix[src.index][dst.index]

    def getSize(self):
        return len(self.a_matrix)

    def addVertex(self, vertex: Vertex):
        size = self.getSize()
        self.a_matrix.append([float(inf)] * size)
        for row in self.a_matrix:
            row.append(float(inf))
        self.vertexes.append(vertex)
        vertex.index = self.i
        self.i += 1
        self.__visited.append(False)

    def addEdge(self, src: int, dst: int, weight=0):
        self.a_matrix[src][dst] = weight
        self.weights += weight
        self.edges.append(Edge(self.vertexes[src], self.vertexes[dst], weight))

    def checkEdge(self, src: int, dst: int):
        if self.a_matrix[src][dst]:
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

    def __dfsPath(self, src: int, dst: int, curr_path: list):
        if self.__visited[src]:
            return
        curr_path.append(self.vertexes[src])
        self.__visited[src] = True
        for i in range(len(self.a_matrix)):
            if self.a_matrix[src][i] is not float(inf):
                if not self.__visited[i]:
                    self.cost.append(self.a_matrix[src][i])
                    self.__dfsPath(i, dst, curr_path)
        if src == dst:
            if self.weights:
                res = sum(self.cost)
                if not self.path or res < self.final_result:
                    self.path = curr_path.copy()
                    self.final_result = res
            else:
                if not self.path or len(curr_path) < len(self.path):
                    self.path = curr_path.copy()

        self.__visited[src] = False
        curr_path.pop()
        if self.cost:
            self.cost.pop()
        return self.path, self.final_result

    def findShortestPath(self, source: int, destination: int):
        cur_path = []
        return self.__dfsPath(source, destination, cur_path)

    def enqueue(self, queue, edges_list):
        for i in range(len(edges_list)):
            if edges_list[i] == 0:
                queue.append(self.vertexes[i])
                edges_list[i] -= 1

    def Kahn(self):
        q = deque()
        edges = len(self.a_matrix) * [0]
        res = []
        for i in range(len(self.a_matrix)):
            for j in range(len(self.a_matrix)):
                if self.a_matrix[i][j] != inf:
                    edges[j] += 1
        self.enqueue(q, edges)
        while q:
            v = q.popleft()
            res.append(v)
            for j in range(len(self.a_matrix)):
                if self.a_matrix[v.index][j] != inf:
                    edges[j] -= 1
            self.enqueue(q, edges)
        return res

    def __repr__(self):
        return f'{self.a_matrix}'


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
    g.addEdge(2, 6, 1)
    g.addEdge(3, 4, 2)
    g.addEdge(3, 5, 5)
    g.addEdge(3, 6, 2)
    g.addEdge(4, 7, 9)
    g.addEdge(5, 7, 1)
    g.addEdge(6, 7, 2)

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
    # print(g.findShortestPath(0, 7))
    print(g.Kahn())
    print(g.edges)
    g.edges.sort()
    print(g.edges)

