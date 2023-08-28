"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Average and count of a list
FILE TYPE   : Average and count of a list
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////////////   Average and count of a list   ////////////////////////
#//////////////////////   Average and count of a list   ////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# User Inputs
#///////////////////////////////////////////
list_1 = input("Dude, give a list of numbers:").split(",")
list_1 = np.array([float(x) for x in list_1])
    
#///////////////////////////////////////////
# Average of a list
#///////////////////////////////////////////

def AverageOfList(List):
    count   = 0
    sum     = 0
    average = 0
    
    for value in List:
        count = count + 1
        sum   = sum + value
    average = sum/count  
    
    return [average, sum, count]

data = AverageOfList(list_1)

print("Dude, the average, the sum and the legnth of yout list are {0}, {1} and {2}".format(data[0],data[1],data[2]))
    