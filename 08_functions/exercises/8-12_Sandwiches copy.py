""" Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time."""

def make_sandwinch(*ingredients):
    """Show the ingredients inside the sandwinch"""
    print("\nThe customer wants the following sandwinch")
    for ingredient in ingredients:
        print(f"- {ingredient}")

make_sandwinch("Jam", "Chesee", "Tomato")
make_sandwinch("Chesee")
make_sandwinch("Lettuce", "Tomato", "Onion")
