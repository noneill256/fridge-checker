# enter food into fridge
# enter dish to cook
  # says if you can cook or not
  # if not, what ingredients are missing?

""" create the dishes here """


""" top menu """
# enter ingredients
# or cook a dish


fridge = []
# use input to append ingredients into fridge


""" cooking """
if fridge == []:
  print('There is nothing in the fridge!')
  
missing = []
# a dish as a list
for ingredient in dish:
  if ingredient in fridge:    
    can_cook = True
  if ingredient not in fridge:
    can_cook = False
    missing.append(ingredient) # creating list of missing ingredients

if can_cook:
  # hurrayyy

if can_cook is False:
  print(f'You are missing the following ingredients for {dish}:') # prints the missing ingredients
  for i in missing:
    print(i)

# back to top menu
