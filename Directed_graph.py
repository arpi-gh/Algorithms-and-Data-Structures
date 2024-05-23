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
        self.rec_stack = []

    def clear_visited(self):
        for i in range(len(self.__visited)):
            self.__visited[i] = False

    def addVertex(self, vertex: Vertex):
        self.a_list.append(vertex)
        vertex.index = self.i
        self.i += 1
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
        neighbors_list = [[] for _ in self.a_list]
        for i in range(len(self.a_list)):
            for vertex in self.a_list[i].neighbors:
                neighbors_list[vertex.index].append(self.a_list[i])
        for vertex in self.a_list:
            vertex.neighbors = neighbors_list[vertex.index]
            print(vertex.neighbors)

    def __hasCycle(self, i):
        self.__visited[i] = True
        self.rec_stack[i] = True
        for n in self.a_list[i].neighbors:
            if self.rec_stack[n.index] or self.__hasCycle(n.index):
                return True
        self.rec_stack[i] = False
        return False

    def hasCycle(self) -> bool:
        self.rec_stack = [False] * len(self.a_list)
        return self.__hasCycle(i=0)

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

    g.addEdge(0, 3)
    g.addEdge(0, 4)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(3, 1)
    g.addEdge(4, 6)
    g.addEdge(5, 7)
    g.addEdge(6, 5)

    # print('First dfs')
    # g.dfs()
    # g.transpose()
    # print('Second dfs')
    # g.clear_visited()
    # g.dfs()
    print(g.hasCycle())





