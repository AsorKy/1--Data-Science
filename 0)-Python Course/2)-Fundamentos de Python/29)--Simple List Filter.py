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
Tresh = float(input("Dude, give me the upper treshold:"))
    
#///////////////////////////////////////////
# Average of a list
#///////////////////////////////////////////

def ListSimpleFilter(List,treshold):
    
    new_list = []
    for value in List:
        if value > treshold:
            new_list = new_list.append(value) 
    
    return new_list

data = ListSimpleFilter(list_1,Tresh)

print("Dude, your new list is")





i = 1
while i < 3:
    print("Mi chino enamorado")
    i = i + 1
    