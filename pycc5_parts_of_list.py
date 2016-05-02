#slicing a list
#to make a slice, specify the index of the first and last elemnts you want to deal with
#python stops one item before the second index you specify

#output first 3 elements in a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#can generate any subset of a list
print(players[1:4])

#can omit the first index in a slice
print(players[:4])

#can omit later indices in a slice
print(players[2:])

#can print starting backwards
print(players[-3:])

#can loop through a slice of a list
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title()) 

#copying lists
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#make a copy by asking for a slice without specifying index

#to prove they are different lists we can append different items
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)