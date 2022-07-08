import fridge as f

def cook():
    """ Asks for dish, then checks for availability of required ingredients """
    # Pre-loading possible dishes :)
    dishes = { 1: {'soba power bowls': ['edamame', 'soba', 'green beans', 'rice vinegar', 'soy sauce', 'sesame oil', 'tofu', 'black bean garlic sauce']},
          2: {'vegetable soup': ['broccoli', 'carrots', 'crushed tomatoes', 'taco seasoning', 'chickpeas', 'garlic', 'onions', 'crushed tomatoes', 'brown rice']},
          3: {'chickpea coconut curry': ['coconut milk', 'chickpeas', 'garam masala', 'cauliflower', 'onions', 'spinach', 'white rice']},
          4: {'general tso tofu': ['general tso sauce', 'tofu', 'broccoli', 'carrots']}
    }
    if f.fr == []:
        print('There is nothing in the fridge!\n')

    # Select the dish to make
    print('\nWhich of the following would you like to make?')
    for key, dish in dishes.items():
        print(f'{key}: ', end='')
        
        for d in dish:
            print(d.title())

    dishnum = input('\nEnter the number of the dish you would like to cook:\n')

    while int(dishnum) not in dishes.keys():
        print('Please enter a valid input.')
        dishnum = input('\nEnter the number of the dish you would like to cook:\n')
    else: # establish the list of required ingredients
        to_cook = dishes[int(dishnum)]
        # a dictionary: key is the dish and value is list of ingredients
        required = []
        for key, values in to_cook.items():
            for value in values:
                required.append(value)
        # now we have the list of required ingredients

    # get the dish name for the final print
    dishname = ''
    for x in to_cook:
        dishname = x   

    # see if we can make the dish. if not, print the list of missing ingredients
    missing = []
    for ingredient in required:
        if ingredient not in f.fr: # if the required ingredient isn't in the fridge
            missing.append(ingredient) # add it to the list of stuff we're missing

    if len(missing) == 0:
            print(f'You can make {dishname}!')
    else:
            print(f'You are missing the following ingredients for {dishname}:') # prints the missing ingredients
            for i in missing:
                print('-',i.title())
            print()












