class holders:
    def __init__(self, desigid, fname, lname, address, holding, issuedate):
        self.desigid = desigid
        self.fname = fname
        self.lname = lname
        self.address = address
        self.holding = holding
        self.issuedate = issuedate

    def __str__(self):
        return f"{self.fname} {self.lname}, {self.address}. Holding: {self.holding}"
    
