# Musikkregister

## Refleksjon og forklaring

---

### Reflesksjon

I dette prosjektet ble vi testet i vår forståelse og kunskap innenfor databaser med mariadb, mysql.connector og koding med Python.
Jeg syntes the var en interresang og vanskelig oppgave som lot meg utforske å lære mye om hvordan man kan automatisere databaser med kode.

Det jeg angrer på mest er at jeg brukte litt lang tid på å kode systemet og tenkte ikke så mye på å ta bilder underveis. Når jeg skulle koble til raspberry pien hjem så fikk jeg en feilmelding og brukte tid på feilsøking. Årsaken til var forsellen mellom nskole og hjemme netverket. Ssh og mariadb brukeren krevde spesefikk ip for å skape en tilkobling. Dette løste jeg ved å gi raspberry pien en ny statisk ip for hjemme nettverket, legge til nye sikkerhets regler i branmuren og endret mariadb brukeren sin host til å akseptere alle iper.

---

### Forklaring

Prosjektet var å lage en database, automatisere opprettelsen av tabeller og gi brukeren en meny som kan utføre forskjellige ting. Med menyen skal brukeren kunne legge til data i tabelene, se dataen, endre på existerende data og slette data.

For å lage koden som kunne oppnå alt dette på en enkel måte brukte jeg disse nødvendige bibliotekene:

1. **Mariadb** for databasen

2. **Dotenv** for å hente .env filens verdier. For eksempel brukernavn og passord.

3. **Readchar** for å få automatisk enter, som at når du trykker for eksempel 1 så automatisk får den signalet å går vidre.
  
Kommando for installasjonen av bibliotekene som brukes i bash terminalen:

`pip install mariadb`

`pip install Dotenv`

`pip install Readchar`


På oppstart av `musikkregister.py` filen så skal den skjekke om du kan koble til mariadb og skjekke om databasen er tilgjengelig. 

Hvis databasen ikke er tilgjengelig oppretter den databasen, så skjekke om tabellene er tilgjengelig og hvis ikke så lager den tabellene. Etter det så spør den om du vil legge til test verdiene som kan bare bli lagdt in hvis tabelene er tomme.

<img width="1512" height="683" alt="image" src="https://github.com/user-attachments/assets/1401197a-de49-40f0-aa15-389371ef828d" />

<img width="227" height="262" alt="image" src="https://github.com/user-attachments/assets/e5176dc2-6df7-4da1-966d-c23188d55a86" />

<img width="533" height="262" alt="image" src="https://github.com/user-attachments/assets/4ea033fd-7d4b-46b9-bd46-c4f21f264cdb" />

<img width="690" height="180" alt="image" src="https://github.com/user-attachments/assets/717ef7a7-2ace-4caf-bdcc-5048f346ece7" />

Hvis du svarer ja til å legge in dataen så settes in testverdiene, så ser tabelene sånn her ut.

<img width="674" height="538" alt="image" src="https://github.com/user-attachments/assets/3f746b08-8e5b-4f2c-9778-10473be184b1" />

Etter du har svart på test spørsmålet og enten lagt inn dataen eller ikke, så hviser den deg menyen. Alternativene er strukturert sånn at den hviser navn først så tallet som hører til alternativet.

<img width="1360" height="435" alt="image" src="https://github.com/user-attachments/assets/ffcecbe0-e36e-4a43-9d32-3ce1ad1c6b01" />

Alternative 1 i menyen er å sette in data i databasen og fungerer som følgende:



Kode liste:

musikkregister.py:

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
```


functions.py:

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
