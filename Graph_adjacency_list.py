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
        self.path = None

    def addVertex(self, vertex: Vertex):
        self.a_list.append(vertex)
        vertex.index = self.i
        self.i += 1
        # print(vertex.index)
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

    # def countLevelNodes(self, level: int, cur_level=1):
    #     res = []
    #     self.q.clear()
    #     self.__visited = [False] * len(self.__visited)
    #     self.q.append(self.a_list[0])
    #     self.__visited[0] = True
    #     last_neighbor = None
    #     completed = True
    #     while self.q:
    #         ver = self.q.popleft()  # 0
    #         if ver is last_neighbor:
    #             completed = True
    #         for n in ver.neighbors:  # 1 2 3
    #             if not self.__visited[n.index]:
    #                 self.q.append(n)
    #                 res.append(n)
    #             self.__visited[n.index] = True
    #             tmp = n
    #         if completed:
    #             last_neighbor = tmp
    #             if cur_level == level:
    #                 return len(res)
    #             else:
    #                 res = []
    #                 completed = False
    #                 cur_level += 1
    #     return 0
    def countLevelNodes(self, level):
        if level == 0:
            print(f'Level {level}: ')
            return 1
        cur_level = 1
        self.q.clear()
        self.__visited = [False] * len(self.a_list)
        self.q.append(self.a_list[0])
        self.__visited[0] = True
        last = self.a_list[0]
        completed = False
        while self.q:
            ver = self.q.popleft()
            if ver is last:
                completed = True
            for n in ver.neighbors:
                if not self.__visited[n.index]:
                    self.q.append(n)
                self.__visited[n.index] = True
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
        res.append(self.a_list[src])
        self.__visited[src] = True
        for n in self.a_list[src].neighbors:
            if not self.__visited[n.index]:
                self.__dfsPath(n.index, dst, res)
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
        return f'{self.a_list}'


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



    # for v in g.a_list:
    #     print(v, v.neighbors)
    # g.bfs()
    # g.dfs()
    # print(g.countLevelNodes(0))
    # print(g.countLevelNodes(1))
    # print(g.countLevelNodes(2))
    # print(g.countLevelNodes(3))
    print(g.findShortestPath(0, 6))



