cars = ['bmw', 'audi', 'toyota', 'subaru']

#permanently changes the order of the list
cars.sort()
print(cars)

#reverses order alphabetically
cars.sort(reverse=True)
print(cars)

#sorted function lets you display list in a certain order but doesn't permanently affect it
brands = ['jordan', 'nike', 'adidas', 'puma']
print("Here is the original list:")
print(brands)

print("\nHere is the sorted list:")
print(sorted(brands))

print("\nHere is the original list again:")
print(brands)

#reverse order of a list
brands.reverse()
print("\n")    
print(brands)

#find length of list
print (len(brands))