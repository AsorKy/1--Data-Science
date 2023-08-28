"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Directories
FILE TYPE   : Dictionary tutorial
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////////  Directory list tutorial  ////////////////////////////
#////////////////////////  Directory list tutorial  ////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////
# User Inputs
#///////////////////////
def run():
    my_dictionary = {
        "key1":1,
        "key2":2,
        "key3":3,       
    }
    
    print(my_dictionary["key1"])

if __name__== "__main__":
    run()
    
    
#///////////////////////
# Another command methods
# .keys() : returns the key of our element
# .values() : returns a list with the dictinary elements
# .items() : returns a list of tuples (key,element)
# .clear() : eliminates all the itesm in the dictionary
# .pop("n") : eliminates the entered element
#///////////////////////


#///////////////////////
# Exmple of a directory

#my_dictionary = {
#    "key1":1,
#    "key2":2,
#    "key3":3,       
#}
#///////////////////////

#///////////////////////
# Another command methods in loops

# loop to obtain the keys of the dictionary

#for characteristic in directory.keys():
#    print(characteristic)

   
# loop to obtain the values of the dictionary

#    for characteristic in directory.values():
#        print(characteristic)

# loop to obtain the items of the dictionary

#    for keys, value in directory.items():
#        print(keys + value)
#///////////////////////