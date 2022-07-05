# enter food into fridge
# enter dish to cook
  # says if you can cook or not
  # if not, what ingredients are missing?

  
import fridge as f, cooking as c


""" top menu """
# enter ingredients or cook a dish
def top_menu():
  command = input("\nEnter 'F' to stock the fridge or 'C' to cook. Enter 'Q' to exit.")

  
""" create the dishes here """
dishes = { 'soba power bowl': ['edamame', 'soba', 'green beans', 'rice vinegar', 'soy sauce', 'sesame oil', 'tofu', 'black bean garlic sauce'],
          'vegetable soup': ['broccoli', 'carrots', 'crushed tomatoes', 'taco seasoning', 'chickpeas', 'garlic', 'onions', 'crushed tomatoes', 'brown rice'],
          'chickpea coconut curry': ['coconut milk', 'chickpeas', 'garam masala', 'cauliflower', 'onions', 'spinach', 'white rice'],
          'general tso tofu': ['general tso sauce', 'tofu', 'broccoli', 'carrots']
}

top_menu() # show the top menu and let user make their first selection

if command.upper() = 'Q':
  # quit

if command.upper() = 'F':
  # run the fridge function? aagh
  f.enter_ingredients()
  top_menu() # after the ingredients are entered, return to the top menu
  
if command.upper() = 'C':
  # run the cook function
  c.cook()
  top_menu() # back to top menu
