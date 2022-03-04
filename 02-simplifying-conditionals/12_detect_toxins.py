"""Exercise 12: Decompose Conditional"""


def make_alert_sound():
    print('made alert sound.')


def make_accept_sound():
    print('made acceptance sound')


def contains_toxin(ingredients):
    return 'sodium nitrate' in ingredients or 'sodium benzoate' in ingredients or 'sodium oxide' in ingredients


ingredients = ['sodium benzoate']
if contains_toxin(ingredients):
    print('!!!')
    print('there is a toxin in the food!')
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()
