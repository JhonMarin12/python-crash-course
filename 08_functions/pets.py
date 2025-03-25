def describe_pet(pet_name:str, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# # Multipe functon calls
# describe_pet('hamster', 'Harry')
# describe_pet('dog', 'willie')

# Keyword arguments
describe_pet(animal_type='hamster', pet_name='Harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Defaul values
describe_pet('willie')