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
envtables = os.getenv("TABLES").split(",")
envtablecontent = os.getenv("TABLECONTENT").split("|")
defaulttable = os.getenv("DEFAULTTABLE")
tested = os.getenv("TESTED")

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
    functions.tablecheck(mycursor, envtables, envtablecontent)
    functions.testinsert(mycursor, mydb, envtables, mariadb)
    functions.nummen(mycursor, mydb)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")