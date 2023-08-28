"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Calculate the gross pay
FILE TYPE   : Calculate the gross pay
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////////   Python Program to calclate a gross pay     ///////////////
#//////////////////   Python Program to calclate a gross pay     ///////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#EXERCISE:
# Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. Pay the hourly rate for the
# hours up to 40 and 1.5 times the hourly rate for all hours worked
# above 40 hours. Use 45 hours and a rate of 10.50 per hour to 
# test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert 
# the string to a number. Do not worry about error checking the
# user input - assume the user types numbers properly. 
# Nevertheless, solve the problem using a try/except command
# to deal with an error.
#///////////////////////////////////////////


#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

hours = input("Enter the number of hours:")
rate = input("Enter the rate:")

try:
    h = float(hours)
    r = float(rate)
except:
    print("Dude, enter a number, no a string.")
    sys.exit()

#///////////////////////////////////////////
#Gross pay calculation
#///////////////////////////////////////////
 
if h > 40:
    extra = h - 40
    pay = 40*r + extra*r*1.5
else:
    pay = 40*r
print("Dude, your salary is {0}" .format(pay))