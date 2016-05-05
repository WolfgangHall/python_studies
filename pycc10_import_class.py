from pycc10_work_with_classes import Car, ElectricCar

my_new_car = Car('ford', 'mustang', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 25
my_new_car.read_odometer()

my_elec_car = ElectricCar('ford', 'prius', 2016)
print(my_elec_car.get_descriptive_name())

#can also import the entire module and use dot notation to access elements