"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Solve the standar quadratic equation
FILE TYPE   : Solve the standar quadratic equation
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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

first = input("Enter a fist name:")
last = input("Enter a last name:")
age = float(input("Enter your age:"))
selection = float(input("Enter your type selection:"))



if selection == 1:
    print("C-STYLE STRING:")
    #///////////////////////////////////////////
    #C-Style string formating
    #///////////////////////////////////////////
    print("Hi dude, nice to meet you mr %s %s" % (first,last) )
    print("as i see, your age is %0.1f" %age)
    #///////////////////////////////////////////
    #.format style
    #///////////////////////////////////////////
else:
    print("F STRING:")
    if selection == 2:
        print("Hi dude, nice to meet you mr {0} {1}" .format(first,last) )
        print("as i see, your age is {0}" .format(age))
    else:
    #///////////////////////////////////////////
    #f.string style
    #///////////////////////////////////////////
        print(f"Hi dude, nice to meet you mr {first} {last}, so you have {age} years old right?")
        

#///////////////////////////////////////////
#NOTES:
    #The %0.nf method consists of mapping a float
    #indexed as "%float" such that the numer of 
    #decimal places to be displayed on the screen 
    #is equal to the number #n# in %0.nf.
#///////////////////////////////////////////