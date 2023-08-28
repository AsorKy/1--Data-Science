"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Map and dictionary transformations
FILE TYPE   : Map function
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
        
        item["taxes"] = item["price"]*.19
        item["total price"] = item["price"] + item["taxes"]
        return item
    
    new_dict = list( map( add_items, list_of_items ) )
    
    return new_dict



if __name__ == "__main__":
    
    prices = values(items)
    new_dir= add_items_to_list(items)
    print(prices)
    print(new_dir)


