"""Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature."""

def car_info(manufacturer:str, model:str,**car_info):
    """Create info about a car"""
    car_info['manufactures'] = manufacturer
    car_info['model'] = model
    return car_info

def show_info(info:dict):
    for key, value in info.items():
        print(f"{key}: {value}")

car =car_info('subaru',
            'F-150',
            color='blue',
            tow_packaje=True
)


show_info(car)