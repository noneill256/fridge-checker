# input the ingredients into a list
fridge = []
ingred = ''
while ingred.upper() != 'Q':
  ingred = input("\nEnter an ingredient. Press 'Q' when finished.")
  if ingred.upper() == 'Q':
    break
  fridge.append(ingred)
