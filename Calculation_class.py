from Warrant_class import warrant
from Result_class import result
import math
from Enum_class import rounding
from DB_class import database

class calculation:
    def __init__(self, warrant_id):
        self.warrant_id = warrant_id
        self._results = []
        self._total = 0
        self.final_results = []


    @property
    def final_results(self):
        return self._final_results

    @final_results.setter
    def final_results(self, value):
        self._final_results = value

    @property
    def warrant_id(self):
        return self._warrant_id
    
    @warrant_id.setter
    def warrant_id(self, value):
        self._warrant_id = value


    @property
    def warrant(self):
        return self._warrant
    
    @warrant.setter
    def warrant(self, value):
        self._warrant = value

    @property 
    def results(self):
        return self._results
    
    @results.setter
    def results(self, value):
        self._results = value

    @property
    def total(self):
        return sum(i.amount for i in self.results)  

    def start(self):
        fetchall = database.retrieve(f"""select StockID, RecordDate, Rate from Warrants where ID = {self.warrant_id}""")

        self.warrant = warrant(self.warrant_id, fetchall[0][0], fetchall[0][1], fetchall[0][2])
        self.warrant.populate_reg()
        self.calculate()
        return self.print_results()      
    
    def calculate(self):
        for i in self.warrant.register:
            choice = (rounding(1))
            match choice:
                case choice.up:
                    amount = math.ceil((float(i.holding) * float(warrant.rate))*100)/100
                    
                case choice.down:
                    amount = math.floor((float(i.holding) * float(warrant.rate))*100)/100
                    
                case choice.middle:
                    amount = round(float(i.holding) * float(warrant.rate), 2)
                    
                case choice.none:
                    amount = float(i.holding) * float(warrant.rate)
            
            self.results.append(result(self.warrant.id, i.desigid , i.holding, amount))

    def print_results(self):
        for result in self.results:
            #result.move_data()
            self.final_results.append(result.ToStr())
        self.final_results.append(f"Total for {warrant.AsAt}: {self.total}")
        return f"Total for {warrant.AsAt}: {self.total}"
        


