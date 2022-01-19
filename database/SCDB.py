import  logging
from    sqlite3 import Error
import  sqlite3

class SCdatabase_SQlite(object):
   
    
    def __init__(self, path= None, DB_name= "SCDB"):
        self.path       = path
        self.DB_name    = DB_name
        self.connection = None

        logging.info(f"Database {self.DB_name} created in {self.path}")

    def connect(self):


        try:
            self.connection = sqlite3.connect(f"{self.DB_name}.sqlite")

            logging.info(f"Connected to database {self.DB_name} in {self.path}.")
    
        except Error as e :

            logging.error(f"The error '{e}' occured during connection.")

        return self.connection
        
    def execute_query(self, query):

        cursor = self.connection.cursor()

        try: 
            cursor.execute(query)
            self.connection.commit()

            logging.info("Query executed successfully") 

        except Error as e:

            logging.error(f"The error '{e}' occurred during executing {query}")

    def execute_read_query(self, query):
        cursor = self.connection.cursor()
        result = None

        try:
            cursor.execute(query)
            result = cursor.fetchall()

            logging.info("Read-Query executed successfully")
            return result
        
            

        except Error as e:
            logging.error(f"The error '{e}' occurred during executing {query}")

class table(object):

    def __init__(self, table_name):
        
        self.table_name    = table_name
        
    
    def create_table_categories(self, categories):
        
        command = f"""CREATE TABLE IF NOT EXISTS {self.table_name} ({categories});"""

        return command
    
    def add_record(self, records):

        command = f"""INSERT INTO {self.table_name} (name, age, gender, nationality) VALUES {records}"""
    
        return command

    def select_record(self, selected= "*"):

        command = f"""SELECT {selected} from {self.table_name}"""

        return command