import pyodbc 
import math

div_list = []

db = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=nevdev.developmentenv.com;"
                      "Database=EC_DEV;"
                      "Trusted_Connection=yes;")

cursor = db.cursor()

def Dividend(ID):
    cursor.execute("""DECLARE @ID INT = ?         
                   select total, Name, Rate from warrants w
                   inner join holdings h on h.stockID = w.stockID
                   where w.ID = @ID and h.issuedate <= w.RecordDate""", ID) 
    fetchall = cursor.fetchall()
    return fetchall

def count_rows(ID):
    fetchall = Dividend(ID)
    return f"Number of records proccessed: {len(fetchall)}"

def calculation(ID):
    fetchall = Dividend(ID)
    total = 0
    count = 0
    while count < len(fetchall):
        dividend = math.floor((float(fetchall[count][0]) * float(fetchall[count][2]))*100)/100
        s = str("dividend for {} = {}p".format(fetchall[count][1], dividend))
        div_list.append(str(s))
        total += dividend
        count+=1

    total = str("Total dividend payments: {}p".format(math.floor(total)/100))
    div_list.append(total)

    return total

def total(ID):
    fetchall = Dividend(ID)
    total = 0
    for i in fetchall:
        total += i[0]
    return f"Total number of stocks proccessed: {total}"


#print('\n'.join(calculation(10)))

