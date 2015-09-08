import numpy as np
# ===================================
class union_grid(object):
    """docstring for union_grid

    n is the number of nodes in the grid

    """
    def __init__(self, n):
        super(union_grid, self).__init__()
        self.n = n
        self.grid = np.arange(0,n,dtype=np.int)

    def connect_slow(self,p,q):
        if self.grid[q]==self.grid[p]:
            print "WARNING they are already connected."
            return 0

        self.grid[np.where(self.grid==self.grid[p])] = self.grid[q]

    def is_connected_quick(self,p,q):
        return self.grid[q]==self.grid[p]
# ===================================
# ===================================

class union_grid_2(object):
    """docstring for union_grid

    n is the number of nodes in the grid

    """
    def __init__(self, n):
        super(union_grid, self).__init__()
        self.n = n
        self.grid = np.arange(0,n,dtype=np.int)


    def root(self,p):
        while self.grid[p]==p:
            p = self.grid[p]
        return p


    def connect_slow(self,p,q):
        rp=self.root[q]
        rq=self.root[p]
        if rp==rq:
            print "WARNING they are already connected."
            return 0

        self.grid[rp] = rq

    def is_connected_quick(self,p,q):
        return self.root[q]==self.root[p]

# ===================================
# ===================================

class union_grid_improved(object):
    """docstring for union_grid

    n is the number of nodes in the grid

    """
    def __init__(self, n):
        super(union_grid_improved, self).__init__()
        self.n = n
        self.grid = np.arange(0,n,dtype=np.int)
        self.tree_sz = np.ones(n,dtype=np.int)


    def root(self,p):
        while self.grid[p]!=p:
            self.grid[p]= self.grid[self.grid[p]]
            p = self.grid[p]
        return p



    def connect_slow(self,p,q):
        rp=self.root(q)
        rq=self.root(p)
        if rp==rq:
            # print "WARNING they are already connected."
            return 0

        if self.tree_sz[rp]<=self.tree_sz[rq]:
            self.grid[rp] = rq
            self.tree_sz[rq]+=self.tree_sz[rp]

        else:
            self.grid[rq] = rp
            self.tree_sz[rp]+=self.tree_sz[rq]



    def is_connected_quick(self,p,q):
        return self.root(q)==self.root(p)
