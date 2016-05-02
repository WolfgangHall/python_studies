digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension
#generate numbers with one line of code

#open a set of brackets and define the expression for values (value ** 2) you want to store
#write a for loop to generate the numbers you want to feed into the expression
#no colon is necessary
squares = [value**2 for value in range(1,11)]
print(squares)