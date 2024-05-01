from Warrant_class import warrant
from Calculation_class import calculation
from DB_class import database

 
def start(identifier):
    fetchall = database.retrieve(f"""select StockID, RecordDate, Rate from Warrants where ID = {identifier}""")

    mywarrant = warrant(id, fetchall[0][0], fetchall[0][1], fetchall[0][2])
    mywarrant.populate_reg()
    calc = calculation(mywarrant)
    calc.calculate()
    return calc.print_results()

#print(start(12))


