"""Exercise 14: Consolidate Conditional Expressions"""


def dice(ingredients):
    print("diced all ingredients.")


def mix_all(diced_ingredients):
    print("mixed all.")


def add_salt():
    print('added salt.')


def pour(liquid):
    print('poured', liquid + '.',)


def has_all_ingredients(ingredients):
    return 'cucumber' in ingredients and 'tomato' in ingredients and 'onion' in ingredients and 'lemon juice' in ingredients
    # Alternate solution (not tested):
    # ingredients_needed = ['cucumber', 'tomato', 'onion', 'lemon juice']
    # if all(ingredient in ingredients for ingredient in ingredients_needed):
    #     return True
    # return False


def make_shirazi_salad(ingredients):
    if not has_all_ingredients(ingredients):
        return

    dice(ingredients)
    mix_all(ingredients)
    add_salt()
    pour('lemon juice')
    print('Your yummy shirazi salad is ready!')


if __name__ == "__main__":
    make_shirazi_salad(['cucumber', 'tomato', 'lemon juice', 'onion'])
