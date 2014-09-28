# coding: utf-8
import numpy as np
u"""
"""


def pcr():
    pass



def _pca(X, factors=None):
    u"""
    [NIPALS function for PCA]
    <INPUTS> X, factors 
        X:          2d ndarray
                        the number of vairables -> m
                        the number of objects   -> n
                        [ [ x[0][0], x[0][1], ...., x[0][m] ],
                        [ x[1][0], x[1][1], ...., x[1][m] ],
                        .
                        [                   ...., x[n][m] ] ]
        factors:    the number of principal components

    <RETURN> (T, P)
        T:          score matrix
        P:          loading matrix
    """

    X_      = X.copy()
    rows    = X_.shape[0]
    cols    = X_.shape[1]

    if factors == None:        
        factors =  cols

    X_res       = X_  # residuals of X
    scores      = []
    loadings    = []
    residuals   = []
     
    for k in range(factors):    
        X_res, t, p = iter_pca(X_res) # execute uni process in nipals iteration.
        scores.append(t)
        loadings.append(p)
        residuals.append( 1 - np.linalg.norm(X_res)**2 / np.linalg.norm(X_)**2 )
    
    P = np.hstack(loadings)
    T = np.hstack(scores)
    Q = residuals

    return (T, P, Q)





def iter_pca(X, epsilon=10**-6):
    u"""
    iterative process of PCA.
    including Cross Validation?
    <INPUTS>
        X:          target matrix.
        epsilon:    the maximum error between delta_u & u
    <RETURN>
        t:          score vector
        p:          loading vecor
        pX          peeled residual
    """

    # to find a variable(column) which has the max variance.
    variances           = [ np.var(X[:,col]) for col in range(X.shape[1])]
    max_variance_col    = variances.index(max(variances))

    # set max variance column as initial score vector.
    u_astah = X[:,max_variance_col][:,np.newaxis]  

    dot_scores     = 1
    while dot_scores > epsilon: # execute plural until residual diff of score vectors is small

        u           = u_astah
        b           = np.dot(X.T, u)            # loading vector
        b           = b / np.linalg.norm(b)
        u_astah     = np.dot(X, b)              # improved score vector
        delta_u     = u_astah - u               # the difference between initial & improved score vector
        dot_scores  = np.dot(delta_u.T, u)

    t   = u_astah               # a score vector
    p   = b                     # a loading vector
    pX  = X - np.dot(t, p.T)    # peeled X matrix

    return (pX, t, p)
     




if __name__ == '__main__':

    import matplotlib.pyplot as plt
    
    
    X = np.random.rand(3, 4)
    T, P, Q = _pca(X)
    plt.plot(Q)
    plt.show()
    


