# coding: utf-8
import numpy as np
u"""
    Data Object
    for Chemometric Analyses

"""




class DataSet:
      
    def __init__(self, Y, X): 
        self._X     = X
        self._Y     = Y

    @property
    def X(self):
        return self._X
 
    @property
    def Y(self):
        return self._Y
          
     


if __name__ == '__main__':


    data = DataSet( Y=np.arange(3),  X=np.arange(9).reshape(3,3) )

   