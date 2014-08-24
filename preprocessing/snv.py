# coding: utf-8
import numpy as np
u"""
    SNV: normalizing
"""

def snv(x):
    u"""
    centering to mean value 
    and normalized by standard deviation
    [args]
        x:    1d-ndarray
    [return]
        normalized x
    """

    mean        = np.mean(x) 
    sigma       = np.std(x)
    x           = (x - mean) / sigma
   
    return x 

    
if __name__ == '__main__':
    pass

