#function definition
#needs no info to do job, therefore nothing in parenthesis
def greet_user():
    #docstring, used to generate documentation for functions
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#can pass info to function
#variable username is a parameter
def greet_player(username):
    print("Hello, " + username.title() + "!")
#value of wolf is an argument
greet_player('wolf')

#positional arguments are simple ways to match each argument in the function call
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('dog', 'sirius')
#can call function multiple times 
describe_pet('cat', 'tabby')

#you can use keyword arguments, by setting a name-value pair
describe_pet(animal_type='hamster', pet_name='harry')

#you can also set default values
def describe_car(car_color, car_brand='toyota'):
    """Display info about car"""
    print("\nI have a " + car_brand.title() + ".")
    print("My " + car_brand.title() + " is " + car_color + ".")
describe_car(car_color = 'red')

#simpler way to use function as it is now positional
describe_car('blue')