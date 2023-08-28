"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : List Comprehention
FILE TYPE   : List Comprehention
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#/////////////////////////   List Comprehention   //////////////////////////
#/////////////////////////   List Comprehention   //////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# List generation
# 
# the general sintaxys is
# [element  for element in iterable]
# [element  for element in iterable if condition]
#///////////////////////////////////////////

#///////////////////////////////////////////
# Simple list generation
#///////////////////////////////////////////

numbers = []
numbers_add2 = []

for element in range(1,11):
    numbers.append(element)

for element in range(1,11):
    numbers_add2.append(element + 2)    

print(numbers)
print(numbers_add2)

numbers_v2 = [element for element in range(1,11)]
numbers_add2_v2 = [element + 2 for element in range(1,11)]

print(numbers_v2)
print(numbers_add2_v2)

#///////////////////////////////////////////
# Conditional list generation
#///////////////////////////////////////////

numbers = [i*2 for i in range(1,20) if i % 2 == 0]
print(numbers)

#///////////////////////////////////////////
# Add elements in a list if certain element is present
#///////////////////////////////////////////

days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

new_list = [element for element in days if "a" in element]
print(new_list)

#///////////////////////////////////////////
# Permutation excercise:
#   You are given three integers x,y and z representing the dimensions of a cuboid 
#   along with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D 
#   grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x , 0<=j<=y and 0<=k<zx. 
#   Please use list comprehensions rather than multiple loops, as a learning exercise.
#///////////////////////////////////////////

if __name__ == "__main__":
    x = int(input("x ="))
    y = int(input("y ="))
    z = int(input("z ="))
    n = int(input("n ="))

rank_1 = range(x + 1)
rank_2 = range(y + 1)
rank_3 = range(z + 1)

permutations =[ [i,j,k] for i in rank_1 for j in rank_2 for k in rank_3 if not i +j + k == n]
print(permutations)
