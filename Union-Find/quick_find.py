'''
Given a list of N integers and n connected components, find if two components are connected
    - Takes only 1 access to find the root of the object N
    - Takes N^2 accesses to perform N union operations on N objects 
'''
from random import randint
from timing import timing


class QF:
    N = 10000
    # unions = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1)]

    # 0  1   2   3   4   5   6   7   8   9
    # ------------------------------------
    # 0  1   2   3   4   5   6   7   8   9  #Roots Init
    # 0  1   2   3   3   5   6   7   8   9  #After First union (4,3)
    # 0  1   2   8   8   5   6   7   8   9  #After Second union (3, 8)
    # 0  1   2   8   8   5   5   7   8   9  #After Third union (6, 5)
    # 0  1   2   8   8   5   5   7   8   8  #After Fourth union (9, 4)
    # 0  1   1   8   8   5   5   7   8   8  #After Fourth union (2, 1)

    def __init__(self):
        self.root = list(range(QF.N))
        # for pair in QF.unions:
        #     self.union(*pair)

    @timing
    def union(self, p: int, q: int):
        # Change root of p to root of q at all occurences
        curr_root = self.root[p]
        new_root = self.root[q]
        for indx, _ in enumerate(self.root):
            if self.root[indx] == curr_root:
                self.root[indx] = new_root

    def connected(self, p: int, q: int) -> bool:
        return self.root[p] == self.root[q]

    def print_roots(self):
        for i, _ in enumerate(self.root):
            print(i, end='\t')
        print()
        for val in self.root:
            print(val, end='\t')
        print()


if __name__ == '__main__':
    qf = QF()
    print(f'For {qf.N} records')
    qf.union(randint(0, qf.N), randint(0, qf.N))


# for 10000 records union operation took - 0.0010 seconds
# for 1 million records union operation took - 0.1065 seconds
# for 100 million records union operation took - 10.7686 seconds
