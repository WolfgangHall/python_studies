current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#letting user choose when to quit
prompt = "\nTell me something, and I wll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

#adding this if statement does not allow the input of 'quit' to
# show up as a message
    if message != 'quit':
        print(message)

#adding a flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)