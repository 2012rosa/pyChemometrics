# coding: utf-8
import numpy as np
u"""
"""



def detrend(y, poly_order):
    u"""
    remove a trend data points have
    you can desinate polynominal order
    of fitting curves(or line) for estimating the trend.
    
    [args]
        x:            1d-ndarray
        poly_order:   polynominal order of fitting curve 
    [return]
        trend removed x
    """
    y_      = y.copy()
    index   = np.arange( len(y) )
    coefs   = np.polyfit( index, y_, poly_order )[:-1]
    
    for order, coef in enumerate(reversed(coefs)):
        for i in range(len(y_)):
            y_[i] -= coef * pow( index[i], order )
    return y_



if __name__ == '__main__':
    
    from fileio.jcamp import read
    import matplotlib.pyplot as plt
    
    x, y            = read('../fileio/testdata/PE1800.DX')
    after       = detrend(y, 1)
    
    plt.plot(x, y, '--')
    plt.plot(x, after)
    plt.show()
    
    