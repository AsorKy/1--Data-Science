"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Conversor de monedas
FILE TYPE   : Function Concepts
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import numpy as np
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////////////   Currency converter  ////////////////////////////
#////////////////////////////   Currency converter  ////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#1)-Currency converter
# Write an algorithm that employs the concept of functions and
# conditionals to conver different types of latinamerican pesos
# to US dolars.
#///////////////////////////////////////////

def coversor (tipo_pesos, valor_dolar):
    pesos = input("Dude, how many" + tipo_pesos + "do you have?:")
    pesos = float(pesos)
    dolar = pesos/valor_dolar
    dolar = str(dolar)
    print("You have $" + dolar + "dolars")
    
menu = """

Welcome to money conversor, you can convert the following currencies:
    1 - Colombian pesos
    2 - Arentine pesos
    3 - Mexican pesos
    
    choose an option:
"""

option = int(input(menu))

if option == 1:
    coversor(" Colombian pesos ", 4600)
elif option == 2:
    coversor(" Argentine pesos ", 65)
elif option == 3:
    coversor(" Mexican pesos ", 24)
else:
    print("Dude, choose 1, 2 or 3, a correct option please")