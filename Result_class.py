from DB_class import database

class result:
    def __init__(self, warrantid, desigid, shares, amount):
        self.warrantid = warrantid
        self.shares = shares
        self.amount = amount
        self.designationid = desigid
        self.command = f"""
        INSERT INTO WarrantResults (designationid, shares, amount, warrantid)
        SELECT {desigid}, {shares}, {amount}, {warrantid}
        WHERE NOT EXISTS (SELECT * FROM WarrantResults WHERE id = {desigid})"""

  
    def move_data(self):
        database.input(self.command)

    def ToStr(self):
        return f"{self.designationid} with {self.shares} is owed {self.amount}"