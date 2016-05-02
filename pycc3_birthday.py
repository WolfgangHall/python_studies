# age = 23
# message = "Happy " + age + "rd Birthday"
# print(message
# above does not work because of difference between str and int

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

lucky_number = 15
message = "My lucky number is " + str(lucky_number) 
print(message)