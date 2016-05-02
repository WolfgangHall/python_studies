motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#changes element in list
motorcycles[0] = 'ducati'
print(motorcycles)

cars = ['ford', 'audi', 'bmw']
print(cars)

#adds element without changing others
cars.append('ferrari')
print(cars)

#can add elements to empty list
languages = []
languages.append('english')
languages.append('german')
languages.append('italian')
print(languages)

#can add a new element at any position
languages.insert(0, 'french')
print(languages)

#remove item from list
names = ['matt', 'mark', 'luke']
print(names)

del names[0]
print(names)

#remove an item using pop()
#pop method removes the last item in a list
#you can work with the item after removing it
systems = ['osx', 'windows95', 'linux']
print(systems)

popped_system = systems.pop()
print(systems)
print(popped_system)

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#can remove by value
dogs = ['hound', 'corgi', 'shepherd']
print(dogs)

dogs.remove('hound')
print(dogs)


toppings = ['pepperoni', 'pineapple', 'anchovies']
too_weird = 'anchovies'
toppings.remove(too_weird)
print(toppings)
print("\n" + too_weird.title() + " is too weird for me.")