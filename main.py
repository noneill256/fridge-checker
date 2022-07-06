# enter food into fridge
# enter dish to cook
  # says if you can cook or not
  # if not, what ingredients are missing?

import fridge as f, cooking as c


# Pre-loading known dishes
dishes = { 'soba power bowl': ['edamame', 'soba', 'green beans', 'rice vinegar', 'soy sauce', 'sesame oil', 'tofu', 'black bean garlic sauce'],
          'vegetable soup': ['broccoli', 'carrots', 'crushed tomatoes', 'taco seasoning', 'chickpeas', 'garlic', 'onions', 'crushed tomatoes', 'brown rice'],
          'chickpea coconut curry': ['coconut milk', 'chickpeas', 'garam masala', 'cauliflower', 'onions', 'spinach', 'white rice'],
          'general tso tofu': ['general tso sauce', 'tofu', 'broccoli', 'carrots']
}

command = ''

while command.upper() != 'Q':
	# The loop ends when 'Q' is entered.
  command = input("\nEnter 'F' to stock the fridge or 'C' to cook. Enter 'Q' to exit.")
	
	if command.upper() = 'F':
		f.enter_ingredients() # run the function to enter ingredients into fridge
		
	if command.upper() = 'C':
		# run the cook function
		c.cook() # check if ingredients meet requirements for recipe
		
	if command.upper() not in ('Q', 'C', 'F'):
		print('That command does not exist.')
  
