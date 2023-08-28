"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Celsius to Fahrenheit and Farenheit to Celsius
FILE TYPE   : Celsius to Fahrenheit and Farenheit to Celsius
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#///////////////////   Python Program  to  convert C to Fh.  ///////////////////
#///////////////////   Python Program  to  convert C to Fh.  ///////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

method = float(input("What do you want to convert, 1 for Celsius, 2 for Fahrenheit:"))
x = float(input("Temperature to convert:"))
conv_fact = 1.8

#///////////////////////////////////////////
# Conversion
#///////////////////////////////////////////

if method == 1:
    fahrenheit = (x * conv_fact) + 32
    print("Brah, %0.3f Celsius is equal to %0.3f Fahrenheit" %( x,fahrenheit ))
else:
    celsius = ( x - 32 ) / conv_fact
    print("Brah, %0.3f Fahrenheit is equal to %0.3f Celsius" %( x,celsius ))