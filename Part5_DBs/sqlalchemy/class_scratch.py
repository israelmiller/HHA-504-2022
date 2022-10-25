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

#Create a new table in the database called 'patient_details'

create_patient_table = """
CREATE TABLE IF NOT EXISTS patient_details (
    id int,
    mrn varchar(255),
    first_name varchar(255),
    last_name varchar(255),
    zip_code varchar(255),
    dob varchar(255),
    gender varchar(255),
    contact_mobile varchar(255),
    contact_home varchar(255),
    PRIMARY KEY (id)
);
"""

create_patient_medications_table = """
CREATE TABLE IF NOT EXISTS patients_medications (
    id int,
    mrn varchar(255),
    medication_id varchar(255),
    PRIMARY KEY (id)
);
"""

create_medications_table = """
CREATE TABLE IF NOT EXISTS medications (
    id int,
    medication_id varchar(255),
    med_ndc varchar(255),
    med_human_name varchar(255),
    med_is_dangerous BOOLEAN,
    PRIMARY KEY (id)
);
"""

create_patient_conditions_table = """
CREATE TABLE IF NOT EXISTS patients_conditions (
    id int,
    mrn varchar(255),
    condition_id varchar(255),
    PRIMARY KEY (id)
);
"""

engine.execute(create_patient_table)
engine.execute(create_medications_table)
engine.execute(create_patient_medications_table)
engine.execute(create_patient_conditions_table)