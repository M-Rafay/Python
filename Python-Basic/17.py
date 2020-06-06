pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.append('at')
print(pets)



responses = {}

polling_active = True
while polling_active:    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

responses[name] = response

repeat = input("Would you like to let another person respond? (yes/ no) ")
if repeat == 'no':
    polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

