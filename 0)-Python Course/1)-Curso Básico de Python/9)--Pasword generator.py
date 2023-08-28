"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Pasword generator
FILE TYPE   : Pasword generator
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random
import string as st
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#///////////////////////////  Pasword generator  ///////////////////////////////
#///////////////////////////  Pasword generator  ///////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
#9)-Pasword generator
# Create an algotihm that generates a pasword using random methods
#///////////////////////////////////////////

def pasword_generator(Lenght, method):
    
    Digits = st.digits
    Lowercases = st.ascii_lowercase
    Uppercases = st.ascii_uppercase
    Symbols    = st.punctuation
    Vocabulary = Digits + Lowercases + Uppercases + Symbols
    
    pasword = []
    
    if method == "while":
        while (len(pasword) < Lenght):
            character = random.choice(Vocabulary)
            pasword.append(character)
    else:
        for i in range(Lenght):
            character = random.choice(Vocabulary)
            pasword.append(character)
            
    pasword = "".join(pasword)
            
    return pasword

    
def run():
    lenght = int(input("Generate a pasword, choose your lenght:"))
    method = input("Choose your method:")
    pasword = pasword_generator(lenght,method)
    print("Your new pasword is:" , pasword)
    
if __name__ == "__main__":
    run()