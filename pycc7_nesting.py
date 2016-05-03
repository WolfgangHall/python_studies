#store a set of dictionaries in a list or a list of items as a value in a dictionary
#can nest a set of dictionaries in a list, a list of items in a dictionary, or
# a dictionary in a dictionary

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#can make code that automatically generates each alien

#make an empty list for storing aliens
aliens = []

#make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15 

#show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens))) 