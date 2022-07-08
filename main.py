# enter food into fridge
# enter dish to cook
# says if you can cook or not
# if not, what ingredients are missing?

import fridge as f, cooking as c



command = ''

while command.upper() != 'Q':
    # The loop ends when 'Q' is entered.
    command = input("Enter 'F' to stock the fridge or 'C' to cook. Enter 'Q' to exit. \n")
	
    if command.upper() == 'F':
    	f.enter_ingredients() # run the function to enter ingredients into fridge
    	
    if command.upper() == 'C':
    	# run the cook function
    	c.cook() # check if ingredients meet requirements for recipe
    	
    if command.upper() not in ('Q', 'C', 'F'):
    	print('Please enter a valid command.')
  
