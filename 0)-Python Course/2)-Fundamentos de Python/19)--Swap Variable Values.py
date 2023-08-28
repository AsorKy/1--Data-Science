"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Swap variable values
FILE TYPE   : Swap variable values
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////   Python Program to Swap two variables  //////////////////
#////////////////////   Python Program to Swap two variables  //////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

X = input("Dude, give me a number x:")
Y = input("Dude, give another number y:")
x_bef = X
y_bef = Y

method = input("Method 1 is swapping by temp variable, method 2 is a direct swap:")

#///////////////////////////////////////////
#Create a temporary variable and swap the values
#///////////////////////////////////////////

if method == 1:
    temp = X
    X = Y 
    Y = temp
else:
    X , Y = Y , X


print("Your input values where x={0} and y={1} ".format(x_bef,y_bef))
print("Dude, the value of x after swapping is: {}".format(X))
print("Dude, the value of y after swaping is {}".format(Y))

