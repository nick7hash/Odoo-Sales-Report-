from google.cloud import bigquery
import pandas as pd
from sqlalchemy import create_engine
import logging
import time
import os
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level = logging.INFO, filename = 'log.log', filemode ='w', format = '%(asctime)s - %(levelname)s - %(message)s')

#----------------------------------------------------Configs--------------------------------------------------
path = "C:/Users/nikhi/Downloads/unimig-data-project-ced40f0b7c88.json"
data = '''
        select * from unimig-data-project.raw_odoo_data.odoo_data
    '''

# ----------------------------------------------------bigquery authentication setup ----------------------------------
def authentication(path, data):
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path
        client = bigquery.Client()
        query = client.query(data)
        dataframe = query.to_dataframe()
        logging.info("Table successfully created and place into the dataframe df")
        return dataframe
    except Exception as e:
        logging.error(f"An error occurred {e}")

#------------------------------------load data to sqlite database ----------------------------------------
def load_sql (df):
    try:
        engine = create_engine('sqlite:///odoo.db')
        start = time.time()
        df.to_sql('Sales', con=engine, if_exists='replace', index = False, method = 'multi', chunksize = 30)
        end = time.time()
        total_time = end - start
        logging.info(f"Data succesfully ingest into our database and total time taken is {total_time}")
    except Exception as e:
        logging.error(f"Ingestion error {e}")


#------------------------------------Main function------------------------------------------------
def main():
    logging.info("Process started")
    df = authentication(path, data)
    load_sql(df)

# ---------------------execution ---------------------------------------
if __name__ == '__main__':
    main()