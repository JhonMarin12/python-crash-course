# Returning a Dictionary

def build_person(firs_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first':firs_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)