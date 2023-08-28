"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Positive or negative number
FILE TYPE   : Positive or negative number
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#///////////////////   Positive or negative number   ///////////////////////////
#///////////////////   Positive or negative number   ///////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

method = float(input("Which loop you want to test?, 1 is for print int loop, 2 if you want to test a beaking out loop, and 3 if you want to test a breaking wout loop with continue:"))

#///////////////////////////////////////////
# Test loops
#///////////////////////////////////////////

if method == 1:
    
    x = float(input("Enter a number:"))
    
    while x > 0:
        print(x)
        x = x - 1
    print("your number is now equal to {}".format(x))
    print("Dude, thanks for test")
    
elif method == 2:
    
    while True:
        line = input("i am done?")
        if line == "done":
            break
        print(line)
    print("done")
    
else:
    
    while True:
        line = input("i am done?")
        if line[0]== "#":
            continue
        if line == "done":
            break
        print(line)
    print("done")
    
        
    
    
    
    
    