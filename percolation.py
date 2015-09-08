import union_find
import numpy as np

class Percolation(object):
    """docstring for Percolation
    1==closed
    0==open
    """
    def __init__(self, n):
        super(Percolation, self).__init__()
        assert n>=0
        self.n = n
        self.matrix = np.ones((n,n),dtype=np.int)
        self.union_grid = union_find.union_grid_improved(n*n+2) # 2 more to allocate the virtual node at the top and at the bottom.
        # link bottom and top row to virtual.
        for x in np.arange(0,n):
            self.union_grid.connect_slow(x,n*n)
        for x in np.arange(n*n-n,n*n):
            self.union_grid.connect_slow(x,n*n+1)

    def open_site(self,i):
        assert i < self.n*self.n and i>=0, 'index out of boundary'
        p,q =np.unravel_index( i, (self.n,self.n))
        # print p,q
        if self.matrix[p,q]==0:
            # print 'return'
            return

        self.matrix[p,q]=0

        if 0<=p+1<self.n and self.matrix[p+1,q]==0 :
            # print np.ravel_multi_index([[p+1],[q]],(self.n,self.n)),p+1,q
            self.union_grid.connect_slow(i,np.int(np.ravel_multi_index([[p+1],[q]], (self.n,self.n))))
        if 0<=p-1<self.n and self.matrix[p-1,q]==0 :
            # print np.ravel_multi_index([[p-1],[q]],(self.n,self.n)),p-1,q
            self.union_grid.connect_slow(i,np.int(np.ravel_multi_index([[p-1],[q]], (self.n,self.n))))
        if 0<=q+1<self.n and self.matrix[p,q+1]==0:
            # print np.ravel_multi_index([[p],[q+1]],(self.n,self.n)),p,q+1
            self.union_grid.connect_slow(i,np.int(np.ravel_multi_index([[p],[q+1]], (self.n,self.n))))
        if 0<=q-1<self.n and self.matrix[p,q-1]==0:
            # print np.ravel_multi_index([[p],[q-1]],(self.n,self.n)),p,q-1
            self.union_grid.connect_slow(i,np.int(np.ravel_multi_index([[p],[q-1]], (self.n,self.n))))

    def is_close(self,i):
        assert i < self.n*self.n and i>=0, 'index out of boundary'
        p,q =np.unravel_index( i, (self.n,self.n))
        return self.matrix[p,q] == 1

    def is_open(self,i):
        assert i < self.n*self.n and i>=0, 'index out of boundary'
        p,q =np.unravel_index( i, (self.n,self.n))
        return self.matrix[p,q] == 0


    def is_full(self,i):
        assert i < self.n*self.n and i>=0, 'index out of boundary'
        return self.union_grid.is_connected_quick(i,self.n*self.n)

    def is_percolating(self):
        return self.union_grid.is_connected_quick(self.n*self.n,self.n*self.n+1)

# GRaphic
    def plot_board(self,fig_n):
        import matplotlib.pyplot as plt
        plt.matshow(np.invert(self.matrix), fignum=fig_n, cmap=plt.cm.gray)


if __name__ == '__main__':
    import time
    import union_find
    import numpy as np
    import matplotlib.pyplot as plt
    import percolation
    n= 25
    ratio = []
    for x in np.arange(1,200):

        indeces = np.random.permutation(n*n)
        perc = percolation.Percolation(n)
        i=0
        # plt.figure(1)
        while (not perc.is_percolating()):
            perc.open_site(indeces[i])
            # perc.plot_board(fig_n=1)
            # plt.show()
            # time.sleep(3)
            # print perc.is_percolating()
            i+=1
        print 1-np.sum(perc.matrix)/float(np.size(perc.matrix))
        ratio.append(1-np.sum(perc.matrix)/float(np.size(perc.matrix)))
        # plt.savefig('test{}.pdf'.format(i))
    print 'mean' , np.mean(ratio)



