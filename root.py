'''
######################################################################
#Packages 
######################################################################
'''
from file_operation import get_filepath_filename_and_load


#determine time of code 
import time
# logs for information
import logging 




def main():
    #measure time of function
    import cProfile
    import pstats
    # sqlite database
    

    # logging definition
    level = logging.DEBUG
    fmt= '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level= level, format= fmt)



    # Create database and connect
    from database.SCDB import SCdatabase_SQlite as SCDB
    from database.SCDB import table as table

    #path = ""

    with cProfile.Profile() as pr:
    
        database = SCDB()
        database.connect()

        # insert table categories
        table_categories = """
        database_id INTEGER PRIMARY KEY AUTOINCREMENT,
        cell_id TEXT NOT NULL,
        operator TEXT,
        solvent TEXT,
        salt TEXT,
        salt_concentration TEXT
        """

        
        table1 = table("self_discharge")
        database.execute_query(table1.create_table_categories(table_categories))

        # add new record
        new_record = """
        ('James', 25, 'male', 'USA'),
        ('Leila', 32, 'female', 'France'),
        ('Brigitte', 35, 'female', 'England'),
        ('Mike', 40, 'male', 'Denmark'),
        ('Elizabeth', 21, 'female', 'Canada');
        """

        database.execute_query(table1.add_record(new_record))

        #select and read records

        content= database.execute_read_query(table1.select_record())
        print(content)

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()
    stats.dump_stats(filename='needs_profiling.prof')








'''
######################################################################
#Main 
######################################################################
'''
if __name__ == '__main__':
    main()

    logging.info("Job done")

