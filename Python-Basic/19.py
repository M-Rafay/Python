def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

a=input("enter first name")
b=input("enter last name")
musician = get_formatted_name(a, b)
print(musician)


def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
        return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)