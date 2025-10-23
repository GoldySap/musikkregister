#Musikkregister

For dette prosjektet skulle jeg lage en musikkregister database. For å gjøre dette brukte jeg disse nødvendige bibliotekene:

1. **Mariadb**

2. **Dotenv**

3. **Readchar**
  
Kommando for installasjons som brukes i bash terminalen:

`pip install mariadb`

`pip install Dotenv`

`pip install Readchar`

På oppstart av `musikkregister.py` filen så skal den skjekke om du kan koble til mariadb, skjekke om databasen er tilgjengelig, opprette databasen hvis den ikke er tilgjengelig, skjekke om tabellene er tilgjengelig og lager tabellene hvi de ikke er tilgjengelig.

Tabellene

Artist tabellen:
| id | artistnavn |
| -- |:---------------:|
| 1 | ACDC |
| 2 | The ink spots |

Song tabellen:
| id | songname | artistid |
| -- |:---------------:|--:|
| 1 | High way to hell | 1 |
| 2 | We'll meet again | 2 |
| 3 | If i didn't care | 2 |

Kode:
```python
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
```

```python
import readchar

options = ["Add content", "View content", "Tests and defaults", "Exit"]
selected = 0
tablename = ""
tablecontent = ""
tablecont = []
val = []

def dbcheck(mycursor, db):
    mycursor.execute("SHOW DATABASES")
    temp = [x[0] for x in mycursor]
    print("Current databases:", temp, "\nDesired database:", db)
    if db not in temp:
      print("Database not found. \nCreating Database...")
      mycursor.execute(f"CREATE DATABASE {db} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
      temp.append(db)
    print(f"Database created: {db}")

def tablecheck(mycursor, db, envtables, envtablecontent, mydb):
    mycursor.execute("SHOW TABLES")
    temp = [x[0] for x in mycursor]
    print("Current tables:", temp, "\nDesired tables:", db)
    if db not in temp:
        print("Tables not found. \nCreating Tables...")
        for i, string in enumerate(envtables):
          x = string
          y = envtablecontent[i]
        mycursor.execute(f"CREATE TABLE {x} {y}")
        mycursor.execute(f"CREATE TABLE {x} {y}")
        print("Tables created.")
    print(f"Tables for {mydb.database}:", temp)

def testinsert(mycursor, mydb, envtables, mariadb):
  val = [
              ("", ""),
              ("", ""),
              ("", ""),
            ]
  print("Test values:", val)
  inp = input("Insert test values? y/n ")
  if inp.lower() == "y":
      try:
          query = f"SELECT COUNT(*) FROM {envtables}"
          mycursor.execute(query)
          row_count = mycursor.fetchone()[0]
          mycursor.execute(f"SELECT * FROM {envtables} LIMIT 0")
          dc = [cl[0] for cl in mycursor.description]
          if "id" in dc:
            dc.remove("id")
          toval = ", ".join(["%s"] * len(dc))
          todc = ", ".join(dc)
          if row_count <= 0:
            print(tablecont)
            testsql = f"INSERT INTO {envtables} ({todc}) VALUES ({toval})"
            mycursor.executemany(testsql, testval)
            mydb.commit()
            print(mycursor.rowcount, "was inserted.")
      except mariadb.Error as e:
          print(f"Error connecting to MariaDB: {e}")

def insert(mycursor, mydb):
    mycursor.execute("SHOW TABLES")
    temp = [x[0] for x in mycursor]
    vs = []
    while True:
        print("Avalible tables:", temp)
        for i, string in enumerate(temp):
          print(f"{string} - {i + 1}")
          vs.append((i + 1, string))
        key = readchar.readkey()
        for number, string in vs:
          if key == number:
            print(f"You chose option: {key}")
            t = string
            ti = 0
            mycursor.execute(f"SELECT * FROM {t} LIMIT 0")
            dc = [cl[0] for cl in mycursor.description]
            if "id" in dc:
              dc.remove("id")
            toval = ", ".join(["%s"] * len(dc))
            todc = ", ".join(dc)
            sql = f"INSERT INTO {t} ({todc}) VALUES ({toval})"
            count = int(input("How many inserts: "))
            for i in range(count):
                ti = ti + 1
                print("\nCurrent insert:", i + 1)
                a = str(input("Song name: "))
                b = str(input("Artist name: "))
                val.append((a, b))
            print(val)
            if val:
              mycursor.executemany(sql, val)
              mydb.commit()
            print("Total inserts:", ti, "added successfully")
        else:
            print(f"{key} is not allowed. Try again:")

def viewer(mycursor):
    mycursor.execute("SHOW TABLES")
    temp = [x[0] for x in mycursor]
    vs = []
    while True:
        print("Avalible tables:", temp)
        for i, string in enumerate(temp):
          print(f"{string} - {i + 1}")
          vs.append((i + 1, string))
        key = readchar.readkey()
        for number, string in vs:
          if key == number:
            return string
        else:
            print(f"{key} is not allowed. Try again:")

def spesifikk(mycursor, t):
    inp = input("View all content? y/n ")
    if inp.lower() == "y":
      mycursor.execute(f"SELECT * FROM {t}")
      for x in mycursor:
        print(x)
    else:
      mycursor.execute(f"SELECT * FROM {t} LIMIT 0")
      dc = [cl[0] for cl in mycursor.description]
      print("Categories:", dc)
      c = input("Which category to search from: ")
      sql = "SELECT * FROM {t} WHERE {c} ='{o}'"
      mycursor.execute(sql)
      res = mycursor.fetchall()
      for x in res:
        print(x)
      cres = list({row["artist"] for row in t})
      print("artists:", cres)
      o = input("What to search for int the category: ")
      if c.lower in dc:
         sql = f"SELECT * FROM {t} WHERE {c} ='{o}'"
         mycursor.execute(sql)
         res = mycursor.fetchall()
         for x in res:
            print(x)
      else:
         print("Invalid search category.")
         spesifikk(t)

def nummen():
    while True:
        print(
            "MusicRegister Menu Options:" \
            "Add content - 1" \
            "View content - 2" \
            "Exit - 3" 
              )
        allowed_keys = {1, 2, 3}
        key = int(readchar.readkey())
        if key in allowed_keys:
            match key:
                case 1:
                    print(f"You chose option: {key}")
                case 2:
                    print(f"You chose option: {key}")
                    t = viewer()
                    spesifikk(t)
                case 3:
                    print(f"You chose option: {key}")
                    break
        else:
            print(f"{key} is not allowed. Try again:")
```
