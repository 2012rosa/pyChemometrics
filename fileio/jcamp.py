# coding: utf-8
u"""
    JCAMP-DX format file read
    http://www.jcamp-dx.org/
"""
import matplotlib.pyplot as plt
import numpy as np
import re



def read(filename):

    file        = open(filename, 'r')
    headers     = []
    datalines   = []
    for line in file:
        if line.find('##') != -1:
            headers.append( line.strip() )
        else:
            datalines.append( line.strip() )
    
    # process headers
    LDR         = read_LDR( headers )
    y_factor    = float( LDR['YFACTOR'] )

    # process XY data 
    xlines = []
    y = []
    for line in datalines:
        values = line.split('+')
        if values[0].strip().isdigit():
            start_x = int(values[0])
            num_x   = len(values[1:])
            end_x   = start_x -  num_x
            x       = np.arange(start_x, end_x, -1)
            xlines.append(x)
            for value in values[1:]:
                y.append( float(value) )
    
    x = np.hstack(xlines) 
    y = np.array(y) * y_factor
    
    return x, y


def read_LDR( header_lines ):
    u"""
        read LDR (LABELLED DATA-RECORD)
    """
    LDR = {} 
    for line in header_lines:
        pattern     = re.search( r'^##(.*)=(.*)$', line )
        if pattern:
            DATA_LABEL_NAME         = pattern.group(1)
            DATA_SET                = pattern.group(2)
            LDR[DATA_LABEL_NAME]  = DATA_SET
    return LDR


def write():
    pass


if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    x, y = read('./testdata/PE1800.DX')
    plt.plot(x, y) 
    plt.show()
    
     