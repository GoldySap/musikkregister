import dotenv
import os
import mariadb
import functions

dotenv.load_dotenv()

#Default Values
envhost = os.getenv("HOST")
envuser = os.getenv("USER")
envpassword = os.getenv("PASSWORD")
envdatabase = os.getenv("DATABASE")
envtables = os.getenv("TABLES")
envtablecontent = os.getenv("TABLECONTENT")
defaulttable = os.getenv("DEFAULTTABLE")

db = envdatabase

try:
    mydb = mariadb.connect(
      host = envhost,
      user = envuser,
      password = envpassword,
    )
    print(mydb)
    print("Connected successfully!")
    mycursor = mydb.cursor()
    functions.dbcheck(mycursor, db)
    mydb = mariadb.connect(
      host = envhost,
      user = envuser,
      password = envpassword,
      database = db,
    )
    print(f"Connected to {db} successfully!")
    mycursor = mydb.cursor()
    functions.tablecheck(mycursor, db, envtables, envtablecontent, mydb)
    functions.nummen()
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")