"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Map function
FILE TYPE   : Map function
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#/////////////////////////////   Map Functions   ///////////////////////////////
#/////////////////////////////   Map Functions   ///////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# Map Function:
# 
#  Create a function that transforms the elements of a list, use a clasic
# approach using def and for commands and traduce this function into another one
# which employs "lambda" and "map".
#///////////////////////////////////////////

numbers = [1,2,3,4]
numbers_2 = [5,6,7]

def transform(lista,factor=2):
    
    lista_2 = []
    
    for i in range( 0, len(lista) ):
        lista_2.append( lista[i]*factor )
    return lista_2


def transform_2(lista,factor=2):
    return list( map( lambda lista: lista*factor, lista ) )



#///////////////////////////////////////////
# Map Function:
# The following code uses two lists to create a transformation
#///////////////////////////////////////////

def transform_3(list_1, list_2):
    
    sumlist = lambda x,y: x + y
    
    return list( map( sumlist, list_1 , list_2  ) )



if __name__ == "__main__":
    numbers2 = transform(numbers,3)
    numbers3 = transform_2(numbers,3)
    numbers4 = transform_3(numbers,numbers_2)
    
    print(numbers2)
    print(numbers3)
    print(numbers4)



