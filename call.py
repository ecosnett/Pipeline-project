from Warrant_class import warrant
from Calculation_class import calculation
 

mywarrant = warrant(7, 0.01, 1, '2024-03-29')
mywarrant.populate_reg()
mywarrant.print_list()
calc = calculation(mywarrant)
calc.calculate()
calc.print_results()
