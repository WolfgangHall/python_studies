#in OOP you write classes that represent real world things and situations
#create objects based on classes
#when you write a class, you define the general behavior of a category of objects
#individual objects is equipped with the general behavior of the class
#making an object from a class is called instantiation
# you work with an instance of a class

#creating a class
#define a class, use capitalized word
class Dog():
    """A simple attempt to model a dog."""

#function that's part of a class is a method
#__init__ method is a special method that runs whenever we create 
# a new instance based on the Dog class
#self parameter is required in the method def,
# self must come first, it's passed automatically
# no need to pass it
    def __init__(self, name, age):
        """Initialize name and age attributes."""
#any variable prefixed with self is available to every method in the class
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

#create an instance of Dog named Willie
my_dog = Dog('willie', 6)

#use dot notation to access information
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

#calling a method
my_dog.sit()
my_dog.roll_over()

#can create as many instances from a class as necessary
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()