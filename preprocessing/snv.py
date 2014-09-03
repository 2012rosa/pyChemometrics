# coding: utf-8
import numpy as np
u"""
    SNV: normalizing
"""

def snv(y):
    u"""
    centering to mean value 
    and normalized by standard deviation
    [args]
        x:    1d-ndarray
    [return]
        normalized x
    """
    y_      = y.copy()
    mean    = np.mean(y_) 
    sigma   = np.std(y_)
    y_      = (y_ - mean) / sigma
   
    return y_ 

    
if __name__ == '__main__':

    from fileio.jcamp import read
    import matplotlib.pyplot as plt
    
    x, y    = read('../fileio/testdata/PE1800.DX')
    after   = snv(y)
    
    plt.subplot(211) 
    plt.plot(x, y)
    plt.subplot(212) 
    plt.plot(x, after)
    plt.show()
    