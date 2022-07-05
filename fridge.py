# input the ingredients into a list
fridge = []
ingred = ''

def enter_ingredients():
""" create a list of available ingredients through input """
  while ingred.upper() != 'Q':
    ingred = input("\nEnter an ingredient. Press 'Q' when finished.")
    if ingred.upper() == 'Q':
      break
    fridge.append(ingred.lower())
