"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Kilometers to miles and miles to kilometers
FILE TYPE   : kilometers to miles and miles to kilometers
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////////   Python Program to  convert km to miles.  /////////////////
#//////////////////   Python Program to  convert km to miles.  /////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

method = float(input("What do you want to convert, 1 for KM, 2 for Miles:"))
x = float(input("Distance to convert:"))
conv_fact = 0.621371

#///////////////////////////////////////////
# Conversion
#///////////////////////////////////////////

if method == 1:
    miles = x * conv_fact
    print("Brah, %0.3f kilometers is equal to %0.3f miles" %(x,miles))
else:
    km = x / conv_fact
    print("Brah, %0.3f miles is equal to %0.3f km" %(x,km))

