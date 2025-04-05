# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested"""
#     for topping in toppings:
#         print(topping)

# make_pizza('pepperoni')
# make_pizza('pepperoni', 'green peppers', 'extra cheese')

def make_pizza(size,*toppings):
    """Summarize the pizza we are about about to make"""
    print(f"\nMaking a {size}-inch pizza with the following topings")
    for topping in toppings:
        print(topping)