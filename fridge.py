# input the ingredients into a list
fr = []

def enter_ingredients():
    ingred = ''
    """ create a list of available ingredients through input """
    while ingred.upper() != 'Q':
        ingred = input("\nEnter an ingredient. Press 'Q' when finished. \n")
        if ingred.upper() == 'Q':
          break
        elif ingred in fr:
            # ensure no repeats
            print('This is already in the fridge!')
        else:
            # add the ingredient to the fridge
            fr.append(ingred.lower())
