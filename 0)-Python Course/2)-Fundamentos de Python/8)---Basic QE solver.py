"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Solve the standar quadratic equation
FILE TYPE   : Solve the standar quadratic equation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import cmath
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////   Python Program to solve the standard quadratic.E     ///////////
#////////////   Python Program to solve the standard quadratic.E     ///////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////
#User Inputs
#///////////////////////////////////////////

a = float(input("Enter the coefficient A:"))
b = float(input("Enter the coefficient B:"))
c = float(input("Enter the coefficient C:"))

#///////////////////////////////////////////
#discriminant calculation
#///////////////////////////////////////////
 
d = (b**2) - (4*a*c) 

if a == 0:
    print("No solution dude, non quadratic equation:")
else:
    sol_1 = (-b - cmath.sqrt(d)) / (2*a)
    sol_2 = (-b + cmath.sqrt(d)) / (2*a)
    print("Dude, the solutions for yout beautiful SQ equation are {0} and {1}" .format(sol_1,sol_2))
