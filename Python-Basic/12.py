message = input("Tell me something, and I will repeat it back to you: ")
print(message.title())

name = input("Please enter your name: ")
print("Hello, " + name.title() + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

