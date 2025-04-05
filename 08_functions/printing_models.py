# Start with somo designs thath need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models
# print("\nThe following models have been printed:")
# for complete_model in completed_models:
#     print(complete_model)

### Restrcuture code using functions
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for complete_model in completed_models:
        print(complete_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = list()

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
print(completed_models)