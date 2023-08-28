"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
AUTHOR      : Nicolas Castillo  
NAME        : Filter function
FILE TYPE   : Filter function
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import sys
import random

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#///////////////////////////////////////////////////////////////////////////////
#////////////////////////////   Filter Function   //////////////////////////////
#////////////////////////////   Filter Function   //////////////////////////////
#///////////////////////////////////////////////////////////////////////////////
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#///////////////////////////////////////////
# Filter Function:
# 
#  Create a function that uses filter() to filter the elements of a list
# and a dictionary.
#///////////////////////////////////////////

numbers = [1,2,3,4,5,6,7,8,9,10]
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]


def even_number_filter(list_of_numbers):
    
    evens = lambda x : x % 2 == 0
    return list( filter( evens, list_of_numbers) )


def winners(list_of_matches):
    
    selector = lambda item : item["home_team_result"] == "Win"
    return list( filter( selector, list_of_matches ) )



if __name__ == "__main__":
    
    new_numbers = even_number_filter(numbers)
    old_numbers = numbers
    new_dict = winners(matches)
    old_dict = matches
    print("*"*10)
    print(new_numbers)
    print("*"*10)
    print(old_numbers)
    print("*"*10)
    print(new_dict)
    print("*"*10)
    print(old_dict)
