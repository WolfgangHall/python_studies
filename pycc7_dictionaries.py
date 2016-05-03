#a collection of key-value pairs
#a set of values associated with each other

alien_0 = {'color': 'green', 'points': 5}

#to get the value associated with a key, give the name of the dictionary
#and place the key inside a set of square brackets
print(alien_0['color'])
print(alien_0['points'])

#access info using code like:
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#dictionaries are dynamic; you can add new pairs
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#starting with an empty dictionary
alien_1 = {}

alien_1['color'] = 'blue'
alien_1['points'] = 10

print(alien_1)

#modifying values in a dictionary
alien_2 = {'color': 'red'}
print("The alien is " + alien_2['color'] + ".")

alien_2['color'] = 'yellow'
print("The alien is " + alien_2['color'] + ".")

alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_3['x_position']))

#move the alien to the right
#determine how far to move the alien based on its current speed

if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#the new position is the old position plus the increment
alien_3['x_position'] = alien_3['x_position'] + x_increment
print("New x-position: " + str(alien_3['x_position']))

#when you no longer need info in dictionary, use the 'del' statement
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


