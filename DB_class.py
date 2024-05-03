import pyodbc 

class database:
    connectionString = "Driver={SQL Server Native Client 11.0}; Server=nevdev.developmentenv.com; Database=EC_DEV; Trusted_Connection=yes;"

    @staticmethod
    def retrieve(command):
            connection  = pyodbc.connect(database.connectionString)
            cursor = connection.cursor()
            cursor.execute(command) 
            data = cursor.fetchall()
            connection.close()
            return data
    
    @staticmethod
    def input(command):
            connection  = pyodbc.connect(database.connectionString)
            cursor = connection.cursor()
            cursor.execute(command) 
            cursor.commit()
            connection.close()

          
          
            

