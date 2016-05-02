#define list, pull a name and store it in the variable magician and print it
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    #every indented line after will happen after the for loop
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#no indent = prints after the for loop is done
print("Thank you, everyone. That was a great magic show!")
