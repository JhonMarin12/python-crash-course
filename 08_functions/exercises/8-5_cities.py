"""Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country"""

def describe_city(city, country='Colombia'):
    print(f"{city.capitalize()} is in {country.capitalize()}")

# Cities in Colombia
describe_city('Medellín')
describe_city('Bogotá')

# City in Mexico
describe_city('Guadalajara', 'Mexico')