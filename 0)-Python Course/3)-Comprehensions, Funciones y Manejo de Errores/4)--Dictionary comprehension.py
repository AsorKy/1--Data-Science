"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Dictionary Comprehention
FILE TYPE   : Dictionary Comprehention
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#//////////////////////   Dictionary  Comprehention   //////////////////////////
#//////////////////////   Dictionary  Comprehention   //////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# Dictionary generation
# 
# the general sintaxys is
# {key:value  for var in iterable}
# {jey:value  for var in iterable if condition}
#///////////////////////////////////////////

#///////////////////////////////////////////
# Simple dictionary generation
#///////////////////////////////////////////


# In the folowing code, the dictionary is created through an iterable
#where the key role is determinated py the i-counter while the value
#by the equality i*2

My_dict ={}

for i in range(1,11):
    My_dict[i] = i*2
    

My_dictV2 = { i:i*2 for i in range(1,11) }

print(My_dict)
print(My_dictV2)

# In the folowing code, we create a dictionary using certain keys and
#certain values within different lists

countries = ["col","mex","bol","pe"]
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
    
populationV2 = { country : random.randint(1, 100) for country in countries}
    
print(population) 
print(populationV2)   
    
    
#///////////////////////////////////////////
# Dictionary generation from two lists
#///////////////////////////////////////////   

# The zip(list1,list2) unifies two lists list1 and list2

names = ["nico","sofi","sebas","cana","vega"]
ages  = [26,23,30,29,26]
unify_list = list(zip(names,ages))

familly = { name:age for (name, age) in zip(names,ages) }

print(familly)

#///////////////////////////////////////////
# Dictionary comprehension with conditionals
#/////////////////////////////////////////// 


# Conditionated Dictionary comprehension generation using a 
#key-list and a disctionary.

countries = ["col","mex","bol","pe"]
populationV2 = { country:random.randint(1, 100) for country in countries }

result = { country:population for (country, population) in populationV2.items() 
          if population >50  }

print(populationV2)
print(result)


# Conditionated Dictionary comprehension generation using a 
#string chain.

text = "I´m Nicolas"
unique_vowels = {c:c.upper() for c in text if c in "aeiou" }
print(unique_vowels)


#///////////////////////////////////////////
# Match the Dictionary elements with an user input
#/////////////////////////////////////////// 

def message_creator(text):
   # Escribe tu solución 👇
   answers ={
      "computadora": "Con mi computadora puedo programar usando Python",
      "celular":"En mi celular puedo aprender usando la app de Platzi",
      "cable":"¡Hay un cable en mi bota!"
   }

   if text in answers.keys():
      return answers[text]
   else:
      return "Artículo no encontrado"  


text = 'computadora'
response = message_creator(text)
print(response)

    

