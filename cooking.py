# import fridge as f???

if f.fridge == []:
  print('There is nothing in the fridge!')
  
print('\nWhich of the following would you like to make?')
for key, value in dishes:
  print(key) # prints the different dishes one can choose from
to_cook = input('\nEnter the dish you would like to cook:')
  
missing = []
# a dish as a list
# modify this to work with a dictionary lol
for ingredient in required:
  if ingredient in fridge:    
    can_cook = True
  if ingredient not in fridge:
    can_cook = False
    missing.append(ingredient) # creating list of missing ingredients

if can_cook:
  # print(f'You can make {dish}!')
  # hurrayyy

if can_cook is False:
  print(f'You are missing the following ingredients for {dish}:') # prints the missing ingredients
  for i in missing:
    print(i)

    
