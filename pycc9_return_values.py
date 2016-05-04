#function does not always display output directly
#return statement takes a value from inside function and sends it to 
# line that called the function

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#when you call a function that returns a value
# you need to provide a variable where the return value can be stored
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('stevie', 'ray', 'vaughn')
print(musician)

#can make a parameter optional
#must make the optional parameter the last element in the arguments list
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

artist = get_formatted_name('pablo', 'picasso')
print(artist)