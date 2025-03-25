"""Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message."""

def make_shirt(size='large', message='I love Python'):
    print(f"The size of the T-shirt is {size}, the message is {message}.")

# Large T-Shirt
make_shirt()

# Medium T-Shirt
make_shirt(size='medium')

# Using kewords arguments
make_shirt(message="We gonna save the world", size="small")