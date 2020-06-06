def greet_user(user_name):
    print("hello! " + user_name.title() + " .")

greet_user("RAFAY")

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
a=input("animal type")
b=input("pet name")
describe_pet(a, b)

