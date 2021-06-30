'''
Given a list of N integers and n connected components, find if two components are connected
    - Takes N array access to find the root with N objects
    - Takes lg N + (cost to find root) accesses to perform union operation with N objects 
    - Takes lg N (base 2 log) accesses to perform connected operation with N objects 
'''
from timing import timing


class QUW:
    N = 1000000
    # unions = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1)]

    # 0  1   2   3   4   5   6   7   8   9
    # -----------Root Values--------------
    # 0  1   2   3   4   5   6   7   8   9  #Initial
    # 0  1   2   3   3   5   6   7   8   9  #After First union (4,3)
    # 0  1   2   8   3   5   6   7   8   9  #After Second union (3, 8)
    # 0  1   2   8   3   5   5   7   8   9  #After Third union (6, 5)
    # 0  1   2   8   3   5   5   7   8   8  #After Fourth union (9, 4)
    # 0  1   1   8   3   5   5   7   8   8  #After Fourth union (2, 1)

    def __init__(self):
        self.root = list(range(QUW.N))
        self.size = [1 for _ in range(QUW.N)]
        # for pair in QUW.unions:
        #     self.union(*pair)

    # @timing
    def union(self, p: int, q: int):
        # Change root of p to root of q
        x = self.get_root(p)
        y = self.get_root(q)

        if x == y:
            return

        if self.size[x] < self.size[y]:
            self.root[p] = y
            self.size[y] += self.size[x]
        else:
            self.root[q] = x
            self.size[x] += self.size[y]

    def get_root(self, i):
        while i != self.root[i]:
            self.root[i] = self.root[self.root[i]]
            i = self.root[i]
        return i

    @timing
    def connected(self, p: int, q: int) -> bool:
        return self.get_root(p) == self.get_root(q)

    def print_roots(self):
        for i, _ in enumerate(self.root):
            print(i, end='\t')
        print()
        for val in self.root:
            print(val, end='\t')
        print()


if __name__ == '__main__':
    quw = QUW()
    nums = list(range(quw.N))
    unions = list(zip(nums[:-1], nums[1:]))

    for pair in unions:
        quw.union(*pair)

    print(f'For {quw.N} records')
    print(quw.connected(0, quw.N-1))

# for 10000 records connected operation took - 0.00000409 seconds
# for 1 million records connected operation took - 0.0000051 seconds
