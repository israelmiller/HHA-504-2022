## load packages for sql class
import pandas as pd
import sqlalchemy
from dotenv import load_dotenv
import os

##load dotenv

load_dotenv()

## load environment variables
MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")


## create connection string
con = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'

## create engine
engine = sqlalchemy.create_engine(con)

## print table names in database
print(engine.table_names())

fakeDataCommand = """
INSERT INTO patient_details VALUES (2, '001', 'john', 'smith', '11790', '11/1/2001', 'male', '631-632-1234', '631-632-1236' )
"""
engine.execute(fakeDataCommand)