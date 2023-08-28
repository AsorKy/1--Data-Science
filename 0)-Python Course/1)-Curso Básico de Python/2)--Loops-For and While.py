"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Powers of a  number
FILE TYPE   : Loop Concepts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////////////  Powers of a number  /////////////////////////////
#////////////////////////////  Powers of a number  /////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#2)-Power of a number
# Write an algorithm that employs the concept of while and for loops to calculate
# diferent powers of a number until certain limit.
#///////////////////////////////////////////


def run_while():
    base = float(input("Hi dude, give me a number: "))
    Limit = int(input("Hi dude, give me a limit:"))
    
    counter = 0
    power = base**counter
    
    while power <= Limit:
        print(str(base) + "to the power of " + str(counter) +
              " is equal to:"+ str(power)
            )
        counter += 1
        power = base**counter
        
        
def run_for():
    base = float(input("Hi dude, give me a number: "))
    Limit = int(input("Hi dude, give me a limit:"))
    
    power = base**0
    
    for i in range(1,Limit):
    
        if power <= Limit:
            print(str(base) + " to the power of " + str(i-1) +
                  " is equal to:" + str(power)
                )  
            power = base**i
        else:
            break  
    

        
if __name__ == "__main__":
    run_while()
    run_for()
    