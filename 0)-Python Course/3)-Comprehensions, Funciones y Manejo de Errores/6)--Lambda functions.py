"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Lambda Functions
FILE TYPE   : Lambda Functions Concept
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////   Lambda Functions   //////////////////////////////
#///////////////////////////   Lambda Functions   //////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# Lambda Functions:
# 
# the general sintaxys is the following, being the function
# 
# def func_name(arguments):
#   return returned_vales
#
# equivalent to
#
# func_name = lambda arguments: returned_value
#///////////////////////////////////////////

x=20

def increment(x):
    return x + 1

increment_V2 = lambda x : x+1

print(x)
print(increment(x))

def full_name(name,last_name):
    return f"Dude your full name is {name.title()} {last_name.title()}"

full_name_V2 = lambda name, last_name : f'Dude your full name is {name.title()} {last_name.title()}'

text = full_name('nicolas', 'castillo ojeda')
text2 = full_name_V2('nicolas', 'castillo ojeda')
print(text)
print(text2)


