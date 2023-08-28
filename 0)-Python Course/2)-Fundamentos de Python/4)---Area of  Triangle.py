"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Area of a triangle
FILE TYPE   : Area of a triangle
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////   Python Program to find the area of a triangle    /////////////
#//////////////   Python Program to find the area of a triangle    /////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////
#input constants, sides of the triangle
#///////////////////////////////////////////

a = float(input("Enter the lenght of side A:"))
b = float(input("Enter the lenght of side B:"))
c = float(input("Enter the lenght of side C:"))

#///////////////////////////////////////////
#calculation of the semi parameter and the area 
#///////////////////////////////////////////

S = (a + b + c) / 2
area = (S*(S-a)*(S-b)*(S-c))**0.5

print("The area of yout triangle is %0.4f" %area)

#///////////////////////////////////////////
#NOTES:
    #The %0.nf method consists of mapping a float
    #indexed as "%float" such that the numer of 
    #decimal places to be displayed on the screen 
    #is equal to the number #n# in %0.nf.
#///////////////////////////////////////////


