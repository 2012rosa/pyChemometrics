# coding: utf-8
import numpy as np
u"""
"""



def detrend(x, poly_order):
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

    index   = np.arange( len(x) )
    coefs   = np.polyfit( index, x, poly_order )
    
    for order, coef in enumerate(reversed(coefs)):
        for i in range(len(x)):
            x[i] -= coef * pow( index[i], order )
    
    return x



if __name__ == '__main__':
    pass

