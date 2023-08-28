"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Gues a number
FILE TYPE   : Text inversion and lower method
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////////////////////  Gues a number  ////////////////////////////////
#//////////////////////////////  Gues a number  ////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#6)-Gues my number
# Create an algotihm that originates a random number and that the user must gues it
# by entering integer number by console
#///////////////////////////////////////////


#///////////////////////
# User Inputs
#///////////////////////

lower_lim = int(input("Hi dude, give me a low numer: "))
upper_lim = int(input("Now dude, give me a high numer: "))


#///////////////////////
# run function
#///////////////////////


def run():
    random_number = random.randint(lower_lim, upper_lim)
    number = int(input("Hi dude, try to gues my int number :v  :"))
    while number != random_number:
        if number < random_number:
            print("nop, a biggerr one...")
        else:
            print("nop, a lower one...")
        number = int(input("Try another one  :"))
    print("¡Congrats dude, you win!")


#///////////////////////
# head
#///////////////////////

if __name__ == "__main__":
    run()