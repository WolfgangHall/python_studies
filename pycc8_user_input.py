message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

#can break down prompts using '+='
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nGreetings, " + name + "!")

age = input("How old are you? ")

#using int() allows us to use comparison math with input numbers
age = int(age)
print(age >= 18)


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride")
else:
    print("\nYou'll be able to ride when you're a little older.")