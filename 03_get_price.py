"""Exercise 3: Replace Temp with Query"""

# Code snippet. Not runnable.
def get_price():
    base_price = get_base_price()
    discount_factor = 0
    if base_price > 1000:
        discount_factor = 0.95
    else:
        discount_factor = 0.98
    return base_price * discount_factor

def get_quantity():
    return 10

def get_item_price():
    return 100

def get_base_price():
    return get_quantity() * get_item_price()
