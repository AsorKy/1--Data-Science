"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Reduce function
FILE TYPE   : Reduce function
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import functools as ft

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////////////   Reduce Function   //////////////////////////////
#////////////////////////////   Reduce Function   //////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# Filter Function:
# 
#  Create a function that uses reduce() to represent a list in a single value
# in which our case should be te accumulation of the summatory of the list elements.
# 
# The reduce() function is a built-in Python 2 function, which takes a set of values
# (a list, a tuple, or any iterable object) as an argument and "reduces" it to a single value. 
# How that single value is obtained from the collection passed as an argument will 
# depend on the function applied.
#
# For example, the following code reduces the list [1, 2, 3, 4] to the number 10 by
# applying the function accum(counter, item), which returns the sum of its arguments.
#
# <
# def accum(counter, item):
# 	return counter + item
#
# print(reduce(accum, [1, 2, 3, 4]))
# >
# 
# The function passed as the first argument must have two parameters. reduce() will
# call it cumulatively (i.e. preserving the result of previous calls) from left to right.
# So the above code is similar to:
#    
# <
# print(accum(accum(accum(1, 2), 3), 4))
# >
#///////////////////////////////////////////

numbers = [1,2,3,4,5,6,7,8,9,10]


def list_accummulator_V1(list_of_numbers):
    
    accumulator = lambda counter, item: counter + item
    return ft.reduce(accumulator, list_of_numbers)


def list_accummulator_V2(list_of_numbers):
    
    def accumulator(counter, item):
        print("counter =>",counter)
        print("item =>",item)
        
        return counter + item
        
    return ft.reduce(accumulator, list_of_numbers)


if __name__ == "__main__":
    
    new_numbers_V1 = list_accummulator_V1(numbers)
    new_numbers_V2 = list_accummulator_V2(numbers)

    print("*"*10)
    print(new_numbers_V1 )
    print("*"*10)
    print(new_numbers_V2 )
    print("*"*10)
