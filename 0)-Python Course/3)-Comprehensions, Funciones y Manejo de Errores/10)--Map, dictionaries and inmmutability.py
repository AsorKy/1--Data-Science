"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Map con inmutabilidad
FILE TYPE   : Map function e inmutabilidad
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#/////////////////////////////   Map Functions   ///////////////////////////////
#/////////////////////////////   Map Functions   ///////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# Map Function:
# 
#  Create a function that extracts the values of a dictionary and that
# add new elements to it. 
#///////////////////////////////////////////

items = [
    {
     "product 1":"T-shirt",
     "price": 100
     },
    {
     "product 2":"Pants",
     "price": 200
     },
    {
     "product 3":"Coat",
     "price": 300
     }
    ]


def values(list_of_items):
    
    key_extractor = lambda item: item["price"]
    return list( map( key_extractor, list_of_items ) )



def add_items_to_list(list_of_items):
    
    def add_items(item):
        
        new_item = item.copy()
        
        new_item["taxes"] = new_item["price"]*.19
        new_item["total price"] = new_item["price"] + new_item["taxes"]
        return item
    
    new_dict = list( map( add_items, list_of_items ) )
    
    return new_dict



if __name__ == "__main__":
    
    prices = values(items)
    new_dir= add_items_to_list(items)
    old_dir= items
    print("*"*10)
    print(prices)
    print("*"*10)
    print(old_dir)
    print(new_dir)
    print("*"*10)