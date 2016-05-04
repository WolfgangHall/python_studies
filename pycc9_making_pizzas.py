#you can import a whole file or a specific function

#importing another file brings all the functions from the file
# ex. module_name.function_name()

import pycc9_pizzas
pycc9_pizzas.make_pizza(16, 'cheese')

from pycc9_pizzas import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'extra cheese', 'pineapple')

#you can also use an alias with 'as' for functions and modules

from pycc9_pizzas import make_pizza as mp
mp(20, 'sausage')

import pycc9_pizzas as p
p.make_pizza(20, 'chicken')
