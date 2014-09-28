# coding: utf-8
u"""
    Savitzky-Golay Smoothing
    http://wiki.scipy.org/Cookbook/SavitzkyGolay
"""
import numpy as np
import math



#def savitzky_golay_each_row( y, half_window, order, deriv ):
def savgol( y, half_window=1, order=1, deriv=0 ):
    u"""
    """
    y_ = y.copy()
    
    B = make_sgtable( half_window, order )
    m = math.factorial(deriv) * np.linalg.pinv(B).A[deriv]
    
    sidevals    = np.zeros(half_window)
    y_          = np.convolve( m, y_, mode='valid')
    #y_          = np.concatenate(( sidevals, y_, sidevals ))
    return y_



def make_sgtable(half_window, order):
    u"""
    
    i: [ 0, 1, 2, ... , order-1, order ]
    k: [-half_window, -half_window+1, ... , 0, ...., half_window, half_window+1]
    
    B: (2*half_window) x (order+1) matrix
        [
            [ (-half_window)**0,    (-half_window)**1,  ... ,   (-half_window)**(order-1),  (-half_window)**(order) ],
            ...
            ..
            [  0**0,                0**1,               ... ,   0**(order-1),               0**(order)          ],
            ..
            ...
            [ (half_window+1)**0,   (half_window)**1,   ... ,   (half_window)**(order-1),   (half_window)**(order)  ]
        ]

    """
    order_range = range( order + 1 )
    B           = np.mat( [[k**i for i in order_range] for k in range(-half_window, half_window+1)] )
    return B




if __name__ == '__main__':
    
    from fileio.jcamp import read
    import matplotlib.pyplot as plt
    
    x, y    = read('../fileio/testdata/PE1800.DX')
    after   = savgol(y, half_window=10)
    after_x = x[10:-10] 
    plt.plot(x, y)
    plt.plot(after_x, after, ':')
    plt.show()
    
    
    