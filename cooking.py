# import fridge as f???
def cook():
""" Asks for dish, then checks for availability of required ingredients """
	if f.fridge == []:
    print('There is nothing in the fridge!')

	print('\nWhich of the following would you like to make?')
	for key, value in dishes:
		print(key) # prints the different dishes one can choose from
	to_cook = input('\nEnter the dish you would like to cook:')

	# if str(to_cook) not in dishes.key ???????????????????
	print('You do not know this recipe.')
	 else:
	  #  to_cook = dishes.to_cook ?????
	  # required = to_cook.values ???????????

	missing = []
	  # a dish as a list
	  # can_cook = True ... is this required here?
	  # modify this to work with a dictionary lol
	for ingredient in required:
		if ingredient not in f.fridge: # if there's even one missing ingredient
		can_cook = False
		missing.append(ingredient) # creating list of missing ingredients

	  	if can_cook:
		# print(f'You can make {dish}!')
		# hurrayyy

	  	if can_cook is False:
			print(f'You are missing the following ingredients for {dish}:') # prints the missing ingredients
			for i in missing:
		  	print(i)


