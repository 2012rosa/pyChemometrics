# coding: utf-8
import numpy as np
from numpy.f2py.crackfortran import dimensionpattern
u"""
    SNV: normalizing
"""


def SNV(X):
    
    dim = len(X.shape)
    if dim == 1:
        return _snv(X) 
    else:
        X_ = X.copy()
        for i, row_x in enumerate(X):
            X_[i] = _snv(row_x)
        
        print X_.shape 
        return X_ 

 
def _snv(x):
    u"""
    centering to mean value 
    and normalized by standard deviation
    [args]
        x:    1d-ndarray
    [return]
        normalized x
    """
    x_      = x.copy()
    mean    = np.mean(x_) 
    sigma   = np.std(x_)
    return    (x_ - mean) / sigma


    
if __name__ == '__main__':

    from fileio.jcamp import read
    import matplotlib.pyplot as plt
    
    x, y    = read('../fileio/testdata/PE1800.DX')
    after   = SNV(y)
    print after
    
    plt.subplot(211) 
    plt.plot(x, y)
    plt.subplot(212) 
    plt.plot(x, after)
    plt.show()
    