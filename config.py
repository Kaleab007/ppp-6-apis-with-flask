import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="Kaleab007",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

  
    cursor = connection.cursor()
  