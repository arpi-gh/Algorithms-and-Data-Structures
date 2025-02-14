class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep == yrep:
            return
        xrank = self.rank[xrep]
        yrank = self.rank[yrep]
        if xrank >= yrank:
            self.parent[yrep] = xrep
            self.rank[xrep] += 1
        else:
            self.parent[xrep] = yrep


if __name__ == '__main__':
    uf = UnionFind(10)

    uf.union(1, 3)
    uf.union(3, 5)
    uf.union(5, 7)
    uf.union(1, 9)

    uf.union(2, 6)
    uf.union(6, 4)
    uf.union(6, 8)

    # Find the representative of each element
    for i in range(10):
        print(f"Element {i} belongs to the set with parent {uf.find(i)}")

