import mysql.connector
import os
import string
import random


MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT")
NO_OF_ROWS = int(os.getenv("NO_OF_ROWS", 100))

def get_name(char_count: int) -> str:
  ran = ''.join(random.choices(string.ascii_uppercase, k = char_count))    
  return ran


if __name__ == "__main__":
  print("START")
  print(MYSQL_HOST)
  print("WRITING TO " + MYSQL_DATABASE + "." + "test_table")
  cnx = mysql.connector.connect(user=MYSQL_USER,
                              password=MYSQL_PASSWORD,
                              host=MYSQL_HOST,
                              port=MYSQL_PORT,
                              database=MYSQL_DATABASE)
  query = "INSERT INTO test_table (first_name, last_name) VALUES (%s, %s);"

  cur = cnx.cursor()
  for i in range(NO_OF_ROWS):
    cur.execute(query, (get_name(12), get_name(8)))
    cnx.commit()
    print("INSERTED", i+1, "row")

  cnx.close()
  print("FINISH")
