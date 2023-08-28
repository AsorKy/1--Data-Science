"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Sets tutorial
FILE TYPE   : Sets concept
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#/////////////////////////   Sets and modifications   //////////////////////////
#/////////////////////////   Sets and modifications   //////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////
# Set functions:
#    
#    add() = it adds an element
#    update() = it adds multiple elements
#    discard() = eliminates an elements if it alreaddy exists 
#    remove() = eliminates an element and if it does not exists it prints "KeyError"
#    pop() = it returns a random element and elminates it, if the set is empty it prints "KeyError"
#    clear() = eliminates everything within the set
     
#///////////////////////////////////////////


#///////////////////////////////////////////
# A set is defines with {} like in the directory cases
# with the difference that a set has o keys
#///////////////////////////////////////////

set_countries = {"col","mex","bol"}
print(set_countries)
print(type(set_countries))

#///////////////////////////////////////////
# A set works only with the class of objects defined within it,
# no matter if in the definition process we have repeated elements.
#///////////////////////////////////////////

set_numbers = {1,2,2,3,1,4,4,5}
print(set_numbers)
print(type(set_countries))

#///////////////////////////////////////////
# A set can work with different data types.
#///////////////////////////////////////////

set_types = {1,2,2,"Hi dude", False}
print(set_types)
print(type(set_types))

#///////////////////////////////////////////
# We can create a set from a different type of object.
#///////////////////////////////////////////

set_from_string = set("Hiii Duuude¡¡")
print(set_from_string)
print(type(set_from_string))

set_from_tuple = set((1,4,2,2,"abc","cbv","as"))
print(set_from_tuple)

numbers = [1,4,3,3,2,10,0]
set_from_list = set(numbers)
print(set_from_list)

unique_numbers = list(set_numbers)
print(unique_numbers)

#///////////////////////////////////////////
# Lenght and element checking of a set
#///////////////////////////////////////////

print("Countries set size: ", len(set_countries))
print("col" in set_countries)
print("peru" in set_countries)

#///////////////////////////////////////////
# Add elements to a set
#///////////////////////////////////////////

set_countries.add("per")
print(set_countries)
set_countries.add("per")
print(set_countries)

#///////////////////////////////////////////
# Set Update, add multiple elements to a list
#///////////////////////////////////////////

set_countries.update({"ch","ecua","ar"})
print(set_countries)

#///////////////////////////////////////////
# Set element elimination
#///////////////////////////////////////////

set_countries.remove("col")
print(set_countries)
#set_countries.remove("arg")
print(set_countries)
set_countries.discard("arg")
print(set_countries)

#///////////////////////////////////////////
# Set elimination
#///////////////////////////////////////////

set_countries.clear()
print(set_countries)