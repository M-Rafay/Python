dimensions = (200,50)
print(dimensions[0])

print(dimensions[1])

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car=="bmw":
        print(car.upper())
    else:
        print(car.lower())


requested_topping = 'mushrooms'
if requested_topping!="anchovies":
    print("hold anchovies")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")



