from Warrant_class import warrant
from Result_class import result
import math
from Enum_class import rounding

class calculation:
    _results = []
    _total = 0
    final_results = []
    def __init__(self, warrant):
        self.warrant = warrant

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
    
    def calculate(self):
        for i in warrant.register:
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
            calculation.final_results.append(result.ToStr())
        calculation.final_results.append(f"Total for {warrant.AsAt}: {self.total}")
        return calculation.final_results 
        


