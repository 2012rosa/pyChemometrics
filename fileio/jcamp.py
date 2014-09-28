# coding: utf-8
u"""
    JCAMP-DX format file read
    http://www.jcamp-dx.org/
"""
import matplotlib.pyplot as plt
import numpy as np
import re




def read(filepath):
    
     
    headers         = []
    datalines       = []
    whole_string    = open_file(filepath)   # open file and get a string
    
    # extract block from ##TITLE to ##END
    envelope_regex  = r'^##TITLE=(.*?)##XYDATA='    # regular expression to extract single jcamp data area
    ldr_block       = re.findall(envelope_regex, whole_string, re.DOTALL)
    ldr_lines       = ldr_block[0].split('\n') 
    ldr_lines       = [ line for line in ldr_lines if len(line)>1 ]
    
    xy_regex        = r'##XYDATA=(.*?)\n(.*?)##END='    # regular expression to extract single jcamp data area
    xy_block        = re.findall(xy_regex, whole_string, re.DOTALL)[0][1]
    xy_lines        = xy_block.split('\n')
    xy_lines        = [ line for line in xy_lines if len(line)>1 ]
      
    for line in ldr_lines:
        if line.find('##') != -1:
            headers.append( line.strip() )

    for line in xy_lines:
        datalines.append( line.strip() )
    
     
    # process headers
    LDR         = read_LDR( headers )
    y_factor    = float( LDR['YFACTOR'] )

    # process XY data 
    xlines  = []
    y       = []
    for line in datalines:
        values = re.split('\+| ', line)
        values = [ val for val in values if len(val)>2 ]
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



def open_file(filepath):
   
    # open file stream
    fobj = open(filepath)
    
    if not fobj:
        print "file doesn't exist."
        return 

    else:
        lines = fobj.read()
        fobj.close()
        return lines 


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



if __name__ == '__main__':
    
    import matplotlib.pyplot as plt
    
    x, y = read('./testdata/PE1800.DX')
    #x, y = read('./testdata/LABCALC.DX')
    plt.plot(x, y) 
    plt.show()
    