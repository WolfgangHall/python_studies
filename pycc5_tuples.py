#tuples are lists that cannot be changed/are immutable
#tuple looks like a lst except you use parentheses instead of square brackets

#if we have a rectangle of a certain size, we can ensure that its size does not change
dimensions = (200, 50)
#use same syntax to access elements in a list
print(dimensions[0])
print(dimensions[1])

#you can loop over tuple using a for loop
for dimension in dimensions:
    print(dimension)

#you can't modify a tuple, but you can overwrite a variable
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)