#python's range function makes it easy to generate a series of numbers
for value in range(1,5):
    print(value)
#range only prints the numbers 1 - 4

#will print out 1 - 5
for value in range(1,6):
    print(value)

#can make a list of numbers by converting range() into variable
numbers = list(range(1,6))
print(numbers)

#can use range() function to skip numbers
even_numbers = list(range(2, 11, 2))
#will constantly add 2 to the value
print(even_numbers)

#will print the first 10 square numbers in a list
#start with empty list called squares
squares = []
#tell Python to loop through each value from 1-10 using range()
for value in range(1,11):
#value is stored as a square
    square = value**2
#each new value is appended
    squares.append(square)
print(squares)