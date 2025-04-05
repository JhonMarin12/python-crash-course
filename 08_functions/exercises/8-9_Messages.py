"""
Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message
"""

messages = ['Hello, How are you?',
            'I like playing videogames',
            "I'm so cold",
            'Bye bye, see ya'
            ]

def show_messages(messages:list[str]):
    """Prints each message from a list of text messages."""
    for message in messages:
        print(message)

# show_messages(messages)

