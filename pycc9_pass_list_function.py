#when you pass a list to a function, the function gets 
# direct access to the contents of the list

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


#a function can modify a list
#any changes made to the list inside the function are permanent

#start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#simulate printing each design, until none are left.
#move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #simulate creating a 3D print from the design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#Display all the completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)