from DB_class import database
from Holders_class import holders

class warrant:
    register = []
    def __init__(self, id, StockID, AsAt, rate):
        warrant.id = id
        warrant.rate = rate
        warrant.StockID = StockID
        warrant.AsAt = AsAt
        warrant.command = f"""select hol.DesignationID, hol.ForeNames, hol.LastName, hol.Address1, h.Total, h.IssueDate from Holders hol
                   inner join holdings h on hol.DesignationID = h.DesignatorID
                   where h.StockID = {StockID} and h.issuedate <= '{AsAt}'"""

    def populate_reg(self):
        fetchall = database.retrieve(warrant.command)
        warrant.register = [holders(row[0],row[1], row[2], row[3], row[4], row[5]) for row in fetchall]
        

    def print_list(self):
        for holder in warrant.register:
                print(holder)











