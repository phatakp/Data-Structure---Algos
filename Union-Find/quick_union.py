'''
Given a list of N integers and n connected components, find if two components are connected
    - Can take N array access to find the root of the object N
    - Takes N + (cost to find root) accesses to perform union operation with N objects 
    - Takes N accesses to perform connected operation with N objects
'''
from timing import timing


class QU:
    N = 10
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
        self.root = list(range(QU.N))
        for pair in QU.unions:
            self.union(*pair)

    # @timing
    def union(self, p: int, q: int):
        # Change root of p to root of q
        self.root[p] = self.get_root(q)

    def get_root(self, i):
        while i != self.root[i]:
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
    qu = QU()

    # unions = list(zip(nums[:-1], nums[1:]))

    # for pair in unions:
    #     qu.union(*pair)

    print(f'For {qu.N} records')
    print(qu.connected(0, qu.N-1))

# for 10000 records connected operation took - 0.0012 seconds
# for 1 million records connected operation took - 0.1462 seconds
