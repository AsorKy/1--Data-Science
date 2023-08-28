"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Lists
FILE TYPE   : List tutorial
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////////////////  Python list tutorial  /////////////////////////////
#//////////////////////////  Python list tutorial  /////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////
# User Inputs
#///////////////////////

my_list_1 = input("Hi dude, give me a list of 5 objects: ").split(",")
my_list_2 = input("Hi dude, give me another list of 5 objects: ").split(",")

my_list_1 = list(float (x) for x in my_list_1)
my_list_2 = list(float(x) for x in my_list_2)


#///////////////////////
# Concatenation vs summatory of lists
#///////////////////////

unified_list = my_list_1 + my_list_2
NPsumed_list = np.array(my_list_1) + np.array(my_list_2)

print("Concatenated list:", unified_list)
print("NP Summerd list:", NPsumed_list)

#///////////////////////
# Slices of lists and reverse methods
#///////////////////////

sl_1 = my_list_1[1:4]
sl_2 = my_list_1[1:]
rev_1 = my_list_1[::-1]
rev_2 = my_list_1.reverse()

print("Sliced list [start,end]:", sl_1)
print("Sliced list [start,until end]:", sl_2)
print("reverse list 1", rev_1)
print("reverse list 2", rev_1)

#///////////////////////
# Extend a list
#///////////////////////

example = ["a"]
example.extend(my_list_1)
ext_1 = example

print("extended list:",ext_1)

#///////////////////////
# Extend a listby multiplication
#///////////////////////

example = ["a"]
ext_2 = example*int(5)

print("extended list by multiplication:", ext_2)

#///////////////////////
# Eliminate the last element of a list
#///////////////////////

my_list_1.pop()
print("Last element elimination:", my_list_1)

#///////////////////////
# list sorting
#///////////////////////

my_list_1.sort()
sortedlist = my_list_1

print("sorted list:", sortedlist)

#///////////////////////
# delete an element of a list
#///////////////////////

del my_list_2[1]

print("Delete an element of a list:", my_list_2)

#///////////////////////
# remove an element of a list if we know which value to remove
#///////////////////////

my_list_1.remove(my_list_1[1])
print("Remove an element of a list:", my_list_1)

#///////////////////////
# Another command methods
# .sorted()
# .clear()
# .count()
# .index()
# .reverse()
# .insert()
# .pop()
# .append()
#///////////////////////

