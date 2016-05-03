cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#one = is used to set a variable
# double == is used for conditional testing
#case does matter 'Audi' != 'audi'

#inequality check
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')

answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')

#using the 'and' and 'or' keyword to check for multiple truths

age = 19
if age > 18:
    print('You are not old enough')