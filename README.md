# Musikkregister

## Refleksjon og forklaring

### Reflesksjon

I dette prosjektet ble vi testet i vår forståelse og kunskap innenfor databaser med mariadb, mysql.connector og koding med Python.
Jeg syntes the var en interresang og vanskelig oppgave som lot meg utforske å lære mye om hvordan man kan automatisere databaser med kode.
Det er fortsatt mye jeg ønsker at jeg hadde fått fullført og endret, som hvordan stukturen er, noen av alternativene, kanskje skrive ut artist navnet sammen med sangen nå man skal se på det i programmet, men desvere blir det til nestegang.

Det jeg angrer på mest er at jeg brukte litt lang tid på å kode systemet og tenkte ikke så mye på å ta bilder underveis. Når jeg skulle koble til raspberry pien hjem så fikk jeg en feilmelding og brukte tid på feilsøking. Årsaken til var forsellen mellom nskole og hjemme netverket. Ssh og mariadb brukeren krevde spesefikk ip for å skape en tilkobling. Dette løste jeg ved å gi raspberry pien en ny statisk ip for hjemme nettverket, legge til nye sikkerhets regler i branmuren og endret mariadb brukeren sin host til å akseptere alle iper.

<img width="1604" height="455" alt="image" src="https://github.com/user-attachments/assets/3dcb2908-4611-4c6f-a75a-bd7bdd61e628" />

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

<img width="856" height="442" alt="image" src="https://github.com/user-attachments/assets/1401197a-de49-40f0-aa15-389371ef828d" />

<img width="227" height="262" alt="image" src="https://github.com/user-attachments/assets/e5176dc2-6df7-4da1-966d-c23188d55a86" />

<img width="533" height="262" alt="image" src="https://github.com/user-attachments/assets/4ea033fd-7d4b-46b9-bd46-c4f21f264cdb" />

<img width="690" height="180" alt="image" src="https://github.com/user-attachments/assets/717ef7a7-2ace-4caf-bdcc-5048f346ece7" />

Hvis du svarer ja til å legge in dataen så settes in testverdiene, så ser tabelene sånn her ut.

<img width="337" height="269" alt="image" src="https://github.com/user-attachments/assets/3f746b08-8e5b-4f2c-9778-10473be184b1" />

Etter du har svart på test spørsmålet og enten lagt inn dataen eller ikke, så hviser den deg menyen. Alternativene er strukturert sånn at den hviser navn først så tallet som hører til alternativet.

<img width="680" height="217" alt="image" src="https://github.com/user-attachments/assets/ffcecbe0-e36e-4a43-9d32-3ce1ad1c6b01" />

Insert
---
"Add content" så spør den deg først om hvilken tabel du vill legge dataen til, så spør den deg om hvor mange ting du vil legge til. For eksempel hvis du valgte tabellen song. Så kommer den til å spøre deg om sang navn og artist for antall ganger du har sagt at du vil legge til data.

<img width="284" height="281" alt="image" src="https://github.com/user-attachments/assets/0387c102-9c0d-483b-b4a9-2eead5852faf" />
<img width="326" height="281" alt="image" src="https://github.com/user-attachments/assets/0ed0c5e0-892e-474b-bbf1-98a00023d536" />
<img width="501" height="281" alt="image" src="https://github.com/user-attachments/assets/45241aa5-d793-446a-bd23-4b7f89b4e2bc" />
<img width="486" height="281" alt="image" src="https://github.com/user-attachments/assets/345fee0d-a129-4630-bb86-865615f97e34" />

Systemmet can også skjekke om for eksempel artisten du prøver å legge til i tabelen allerede ligger i tabellen.

<img width="328" height="281" alt="image" src="https://github.com/user-attachments/assets/f88b2d25-bd9c-4f9d-8d36-e027fc2dcb7e" />


Viewing
---
"View content" så spør den deg først om velge en tabel og så gir deg 3 valg. 

Det første valg er "View all content" som hviser all dataen som ligger i tabellen.

<img width="649" height="690" alt="image" src="https://github.com/user-attachments/assets/2b80ccc6-9e7b-4a32-bf33-f197528c580d" />

Andre valget heter "Search category content" og lar deg se alt innen for en spesifikk kategori/kolonne.

<img width="661" height="729" alt="image" src="https://github.com/user-attachments/assets/b1f57725-417d-4983-aa7d-7f07fd3225c1" />

Tredje valget er "Search spesifikk content" som lar deg søke etter en spesefikk rad innenfor en spesefikk kolonne.

<img width="661" height="776" alt="image" src="https://github.com/user-attachments/assets/96906893-79b6-48bc-b707-1d8f2d58a0da" />


Updating/altering
---

Deletion
---
"Deletion options" gir deg 3 forskjellige alternativer for å slette data.

1. "Delete specific data" lar deg søke etter en spesefikk rad, lignende hvordan man søker med "View content" alternativet, og så sletter det. Denne skjekker også hva du sletter og justerer stukturen. Hvis jeg sletter en artist med flere sanger så kan jeg enten slette artisten og alle sangene samtidig, eller slette artisten og gjøre artisten til sangene usjent.

<img width="704" height="309" alt="image" src="https://github.com/user-attachments/assets/32efcb84-6bb4-44f7-8bcf-992ebb5c8ad4" />
<img width="687" height="341" alt="image" src="https://github.com/user-attachments/assets/d0c1c5df-5ab7-4358-a5c1-ff3990ef5686" />

2. "Wipe all data (clear all tables)" sletter all dataen fra tabelene og nullstiller idene.

<img width="754" height="555" alt="image" src="https://github.com/user-attachments/assets/5df87b84-6e6b-449e-8511-e98bf7f90d24" />


3. "Delete database" fjerner databasen, som fjerner alle tabelene og all dataen inni databasen. Så til slutt stenger programmet.

<img width="444" height="312" alt="image" src="https://github.com/user-attachments/assets/bf548bed-f45e-4320-903a-7f4b59cfaa39" />

Exiting
---
Hvis du velger "Exit" så lokker den programmet.

<img width="778" height="382" alt="image" src="https://github.com/user-attachments/assets/2de7b57f-58f9-4025-ad2a-aa06e3fe3b7e" />



Kode liste:
---
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

def tselector(mycursor):
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
                    t = tselector()
                    spesifikk(t)
                case 3:
                    print(f"You chose option: {key}")
                    break
        else:
            print(f"{key} is not allowed. Try again:")
```
