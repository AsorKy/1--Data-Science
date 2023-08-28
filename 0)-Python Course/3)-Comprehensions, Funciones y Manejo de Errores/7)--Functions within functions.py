"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Higher order Functions
FILE TYPE   : Higher order Functions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////////   Higher Order Functions   ///////////////////////////
#////////////////////////   Higher Order Functions   ///////////////////////////
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
#
# Create a simple program that uses a function within a function
#together with the concept of lambda functions.
#///////////////////////////////////////////


def increment(x):
    return x + 1

increment_V2 = lambda x : x + 1

def high_ord_func(x, func):
    return x + func(x)

high_ord_func_V2 = lambda x, func: x + func(x)

if __name__ == "__main__":
    
    x_num = float(input("Hi dude, give me a number:"))
    
    result = high_ord_func( x_num, increment )
    result2 = high_ord_func_V2( x_num, increment_V2 )
    print(result)
    print(result2)