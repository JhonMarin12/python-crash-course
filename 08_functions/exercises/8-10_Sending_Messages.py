"""
Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed.
After calling the function, print both of your lists to make sure the messages were moved correctly
"""

messages = ['Hello, How are you?',
            'I like playing videogames',
            "I'm so cold",
            'Bye bye, see ya'
            ]

sent_messages = []

def show_messages(messages:list[str]):
    """Prints each message from a list of text messages."""
    for message in messages:
        print(message)

def send_messages(messages:list[str], sent_messages):
    """Simulate the action of to send a message"""
    while messages:
        current_message = messages.pop()
        print(f"Sending Message:{current_message}")
        sent_messages.append(current_message)

send_messages(messages, sent_messages)

print("Checking results")
print(messages)
print(sent_messages)