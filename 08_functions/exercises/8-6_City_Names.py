"""Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
"Santiago, Chile
Call your function with at least three city-country pairs, and print the values that are returned."""

def city_country(city, country):
    """Return a formatted string with the city and country in 'City, Country' format."""
    print(f"{city.capitalize()}, {country.capitalize()}")

city_country('Bogotá', 'Colombia')
city_country('Caracas', 'Venezuela')
city_country('Buenos Aires', 'Argentina')