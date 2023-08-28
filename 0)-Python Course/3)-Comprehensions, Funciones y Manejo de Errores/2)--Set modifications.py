"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Set operations
FILE TYPE   : Set operations
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
#    union() or | = union set of two sets
#    intersection() or & = intersection set of two sets
#    difference() or - = difference set between two sets, residual set of A 
#                         by eliminating the common elements with B
#    symmetric_difference() or ^ = union difference set of two sets 
    
#///////////////////////////////////////////

#///////////////////////////////////////////
# Union set between two sets
#///////////////////////////////////////////

set_a = {"col","mex","bol"}
set_b = {"pe","bol"}

set_c = set_a.union(set_b)
set_c_2 = set_a | set_b

print(set_c)
print(set_c_2)

#///////////////////////////////////////////
# Intersection set between two sets
#///////////////////////////////////////////

set_a = {"col","mex","bol"}
set_b = {"pe","bol"}

set_c = set_a.intersection(set_b)
set_c_2 = set_a & set_b

print(set_c)
print(set_c_2)

#///////////////////////////////////////////
# Difference set between two sets
#///////////////////////////////////////////

set_a = {"col","mex","bol"}
set_b = {"pe","bol"}

set_c = set_a.difference(set_b)
set_c_2 = set_a - set_b

print(set_c)
print(set_c_2)

#///////////////////////////////////////////
# Symmetric set between two sets
#///////////////////////////////////////////

set_a = {"col","mex","bol"}
set_b = {"pe","bol"}

set_c = set_a.symmetric_difference(set_b)
set_c_2 = set_a ^ set_b

print(set_c)
print(set_c_2)

#///////////////////////////////////////////
# Example of multiple union sets
#///////////////////////////////////////////

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}


new_set = countries | northAm | centralAm | southAm
print(new_set)

new_set = countries.union(northAm,centralAm,southAm)
print(new_set)