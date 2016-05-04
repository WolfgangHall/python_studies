class Car():
    """A simple attempt to represent a car."""

#define the __init__() method with the self parameter
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
    # every attribute in a class needs an initial value
    # whether its empty string or 0
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("This function only increases the mileage!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#attributes can be modified in three ways:
# change the value directly through an instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# set the value through a method
# see update.odometer() function, must pass in new value as argument
my_new_car.update_odometer(23)
my_new_car.read_odometer()

# increment the value through a method
my_new_car.increment_odometer(100)
my_new_car.read_odometer()