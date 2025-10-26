# Musikkregister

## Refleksjon og forklaring

### Reflesksjon

I dette prosjektet ble vi testet i vår forståelse og kunskap innenfor databaser med mariadb, mysql.connector og koding med Python.
Jeg syntes the var en interresang og vanskelig oppgave som lot meg utforske å lære mye om hvordan man kan automatisere databaser med kode.
Det er fortsatt mye jeg ønsker at jeg hadde fått fullført og endret, som hvordan stukturen er, noen av alternativene, kanskje skrive ut artist navnet sammen med sangen nå man skal se på det i programmet, fikse update/alter duplikatetet som blir rart for en eller annen grunn, men desvere blir det til nestegang. Dette dokumente mangler også noe info om hvordan koden fult funker og kunne ha sett bedre ut. Er også ufornøyd med oppsettet av dokumentasjonen. Jeg hadde likt å starte hvert segment med en forklaring/opplysning der jeg henviser til koden og forklarer den funksjonalitet, og har bilder av resultatet med forklaringer til slutt for å vise at den funker.

Det jeg angrer på er at jeg brukte litt lang tid på å kode systemet og tenkte ikke så mye på å ta bilder underveis. Når jeg skulle koble til raspberry pien hjem så fikk jeg en feilmelding og brukte tid på feilsøking. Årsaken til var forsellen mellom skole og hjemme netverket. Ssh og mariadb brukeren krevde spesefikk ip for å skape en tilkobling. Dette løste jeg ved å gi raspberry pien en ny statisk ip for hjemme nettverket, legge til nye sikkerhets regler i branmuren og endret mariadb brukeren sin host til å akseptere alle iper.

<img width="1604" height="455" alt="image" src="https://github.com/user-attachments/assets/3dcb2908-4611-4c6f-a75a-bd7bdd61e628" />

---

### Forklaring

I denne forklaringen rekker jeg ikke dekket alt av hva koden min gjør, men listen av den fulle koden er på bunnen av dokumentet.

Prosjektet var å lage en database, automatisere opprettelsen av tabeller og gi brukeren en meny som kan utføre forskjellige ting. Med menyen skal brukeren kunne legge til data i tabelene, se dataen, endre på existerende data og slette data.

Hovedfilene er musikkregister.py og functions.py, archive.py er et arkive der jeg har min test og gammel kode

For å lage koden som kunne oppnå alt dette på en enkel måte brukte jeg disse nødvendige bibliotekene:

1. **Mariadb** for databasen

2. **Dotenv** for å hente .env filens verdier. For eksempel brukernavn og passord.

3. **Readchar** for å få automatisk enter, som at når du trykker for eksempel 1 så automatisk får den signalet å går vidre.
  
Kommando for installasjonen av bibliotekene som brukes i bash terminalen:

`pip install mariadb`

`pip install Dotenv`

`pip install Readchar`


På oppstart av `musikkregister.py` filen så skal den skjekke om du kan koble til mariadb og skjekke om databasen er tilgjengelig.For inloggingsdetaljene brukte jeg en .env fil og har exludert den fra dette repositoriet med en .gitignore file for sikkerhet. Hvis databasen ikke er tilgjengelig oppretter den databasen, så skjekke om tabellene er tilgjengelig og hvis ikke så lager den tabellene. Etter det så spør den om du vil legge til test verdiene som kan bare bli lagdt in hvis tabelene er tomme.

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
"Update/alter content" lar deg velge tabel, så navnet på hva du vil endre, også det nye navnet den skal ha. Den skjekker også om for eksempel om en artist du skal endre har noen sanger som trenger artisten, og hvis det er noen sanger så spør den deg om hvordan du vil håndtere det.

Første alternative er å bytte navn på artisten og slette alle sangene artisten hadde.

<img width="848" height="619" alt="image" src="https://github.com/user-attachments/assets/421b006d-a7af-4767-afc6-9b8fe6c3cff5" />
<img width="690" height="503" alt="image" src="https://github.com/user-attachments/assets/2dd3b9d9-213b-4707-b792-8cc99cc3d741" />

Andre alternativ er å endre navnet på artisten, men lage en duplikat av det gammle navnet som brukes til å lage en ny rad med data og kobles til sangene av den artisten. 
Det gjenstår bare et lite problem som er at når duplikaten skapes så leges den til så (2, artistnavn) istedenfor å bare ha artist navnet.

<img width="853" height="624" alt="image" src="https://github.com/user-attachments/assets/b8af1980-7be9-4388-8a30-23f080915858" />

<img width="694" height="556" alt="image" src="https://github.com/user-attachments/assets/b2dd5d42-28e6-4e28-8627-305d451c7fd1" />


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

def dbcheck(mycursor, db):
    mycursor.execute("SHOW DATABASES")
    temp = [x[0] for x in mycursor]
    print("Current databases:", temp, "\nDesired database:", db)
    if db not in temp:
      print("Database not found. \nCreating Database...")
      mycursor.execute(f"CREATE DATABASE {db} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
      temp.append(db)
    print(f"Database created: {db}")

def tablecheck(mycursor, envtables, envtablecontent):
    mycursor.execute("SHOW TABLES")
    temp = [x[0] for x in mycursor]
    print("Current tables:", temp, "\nDesired tables:", envtables)
    for i, tablename in enumerate(envtables):
      con = envtablecontent[i]
      if tablename not in temp:
          print(f"Table '{tablename}' not found. Creating table...")
          try:
              mycursor.execute(f"CREATE TABLE {tablename} {con}")
              print(f"Table '{tablename}' created successfully.")
          except Exception as e:
              print(f"Error creating table '{tablename}': {e}")
      else:
          print(f"Table '{tablename}' already exists.")
    print("All desired tables present.")

def testinsert(mycursor, mydb, envtables, mariadb):
  val = [
              ("acdc", "high way to hell"),
              ("the ink spots", "we'll meet again"),
              ("the ink spots", "if i didn't care"),
            ]
  print("Test values:", val)
  inp = input("Insert test values? y/n ").lower()
  if inp.lower() != "y":
      print("Cancelled.")
      return
  try:
      atable = None
      stable = None
      for t in envtables:
          if "artist" in t.lower():
              atable = t
          elif "song" in t.lower():
              stable = t
      if not atable or not stable:
          print("Error: Could not find 'artist' or 'song' table in envtables.")
          return
      mycursor.execute(f"SELECT COUNT(*) FROM {atable}")
      artist_count = mycursor.fetchone()[0]
      if artist_count == 0:
          print("Inserting test artists...")
          unique_artists = list({artist for artist, _ in val})
          artist_inserts = [(artist,) for artist in unique_artists]
          mycursor.executemany(f"INSERT INTO {atable} (artistname) VALUES (%s)", artist_inserts)
          mydb.commit()
          print(f"{mycursor.rowcount} artists inserted.")
      else:
          print("Artists already exist, skipping artist insert.")
      mycursor.execute(f"SELECT COUNT(*) FROM {stable}")
      song_count = mycursor.fetchone()[0]
      if song_count == 0:
          print("Inserting test songs...")
          mycursor.execute(f"SELECT id, artistname FROM {atable}")
          artist_map = {name.lower(): aid for aid, name in mycursor.fetchall()}
          sints = []
          for artistname, songname in val:
              aid = artist_map.get(artistname.lower())
              if aid:
                  sints.append((songname, aid))
              else:
                  print(f"Warning: Artist '{artistname}' not found, skipping song '{songname}'")
          if sints:
              mycursor.executemany(f"INSERT INTO {stable} (songname, artistid) VALUES (%s, %s)", sints)
              mydb.commit()
              print(f"{mycursor.rowcount} songs inserted.")
      else:
          print("Songs already exist, skipping song insert.")
      print("Test insert completed successfully.")
  except mariadb.Error as e:
      print(f"Error connecting to MariaDB: {e}")

def insert(mycursor, mydb):
    t = tselector(mycursor)
    print(f"\nSelected tabel: {t}")
    if t == "artist":
        count = int(input("How many artist to add: "))
        for _ in range(count):
          aname = input("Artistname: ").lower()
          mycursor.execute("SELECT id FROM artist WHERE artistname = %s", (aname,))
          res = mycursor.fetchone()
          if res:
              print(f"Artist: '{aname}' already exist.")
          else:
              mycursor.execute("INSERT INTO artist (artistname) VALUES (%s)", (aname,))
              mydb.commit()
              print(f"Artist '{aname}' added.")
    elif t == "song":
        count = int(input("How many song to add: "))
        for _ in range(count):
          sname = input("Songname: ").lower()
          aname = input("Artistname: ").lower()
          mycursor.execute("SELECT id FROM artist WHERE artistname = %s", (aname,))
          res = mycursor.fetchone()
          if res:
              aid = res[0]
          else:
              mycursor.execute("INSERT INTO artist (artistname) VALUES (%s)", (aname,))
              mydb.commit()
              aid = mycursor.lastrowid
              print(f"Artist '{aname}' added automatically.")
          mycursor.execute(
              "INSERT INTO song (songname, artistid) VALUES (%s, %s)",
              (sname, aid)
          )
          mydb.commit()
          print(f"Song: '{sname}', added with artist: '{aname}'.")

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
        if key.isdigit():
          key = int(key)
          for number, string in vs:
            if key == int(number):
              return string
            else:
              print(f"Invalid {key}. Try again:")

def spesifikk(mycursor, t):
  while True:
      print(
      "\nSearch Options:" \
      "\nView all content - 1" \
      "\nSearch category content - 2" \
      "\nSearch spesifikk content - 3"
        )
      key = readchar.readkey()
      if key.isdigit():
        key = int(key)
        match key:
          case 1:
              print(f"\nYou chose option: {key}\n")
              mycursor.execute(f"SELECT * FROM {t}")
              res = mycursor.fetchall()
              for x in res:
                print(x)
              break
          case 2:
              print(f"\nYou chose option: {key}\n")
              mycursor.execute(f"SELECT * FROM {t} LIMIT 0")
              dc = [cl[0] for cl in mycursor.description]
              if "id" in dc:
                dc.remove("id")
              print("Categories:", dc)
              c = input("Which category to search from: ")
              sql = f"SELECT {c} FROM {t};"
              mycursor.execute(sql)
              res = mycursor.fetchall()
              for x in res:
                print(x)
              break
          case 3:
              print(f"\nYou chose option: {key}\n")
              mycursor.execute(f"SELECT * FROM {t} LIMIT 0")
              dc = [cl[0] for cl in mycursor.description]
              if "id" in dc:
                dc.remove("id")
              print("Categories:", dc)
              c = input("Which category to search from: ")
              sql = f"SELECT {c} FROM {t};"
              mycursor.execute(sql)
              res = mycursor.fetchall()
              for x in res:
                print(x)
              o = input("What to search for in the category: ")
              if any(o.lower() == str(x[0]).lower() for x in res):
                sql = f"SELECT * FROM {t} WHERE {c} = %s"
                mycursor.execute(sql, (o,))
                res = mycursor.fetchall()
                for x in res:
                  print(f"{x}")
              else:
                print("Invalid search. Try again.")
          case _:
            print(f"\n{key} is not allowed. Try again.\n")
      else:
        print(f"\n{key} is not allowed. Try again.\n")

def alter(mycursor, mydb, t):
  while True:
    if t.lower() == "artist":
        c = "artistname"
        sql = f"SELECT {c} FROM {t};"
        mycursor.execute(sql)
        res = mycursor.fetchall()
        for x in res:
          print(x)
        name = input("Artist name to modify: ").strip()
        mycursor.execute(f"SELECT id, {c} FROM {t} WHERE artistname = %s", (name,))
        artist = mycursor.fetchone()
        if not artist:
            print("Artist not found.")
        artist_id = artist[0]
        new_name = input("New artist name: ").strip()
        mycursor.execute("SELECT COUNT(*) FROM song WHERE artistid = %s", (artist_id,))
        linked_songs = mycursor.fetchone()[0]
        if linked_songs > 0:
            print(f"\nArtist '{name}' has {linked_songs} linked song(s)." \
                  "\nRename artist and delete songs. - 1" \
                  "\nRename artist, make a duplicate of the old artist and reassign songs. - 2" \
                  "\nCancel. - 3"
                  )
            key = readchar.readkey()
            if key.isdigit():
              key = int(key)
              match key:
                case 1:
                    mycursor.execute("DELETE FROM song WHERE artistid = %s", (artist_id,))
                    mycursor.execute("UPDATE artist SET artistname = %s WHERE id = %s", (new_name, artist_id))
                    mydb.commit()
                    print(f"Renamed artist '{name}' to '{new_name}'")
                    break
                case 2:
                    mycursor.execute("INSERT INTO artist (artistname) VALUES (%s)", (artist,))
                    mydb.commit()
                    aid = mycursor.lastrowid
                    mycursor.execute("UPDATE song SET artistid = %s WHERE artistid = %s", (aid, artist_id))
                    mydb.commit()
                    mycursor.execute("UPDATE artist SET artistname = %s WHERE id = %s", (new_name, artist_id))
                    mydb.commit()
                    print(f"Created new artist '{new_name}' and reassigned all songs.")
                    break
                case _:
                    print("Cancelled.")
                    break
        else:
            mycursor.execute("UPDATE artist SET artistname = %s WHERE id = %s", (new_name, artist_id))
            mydb.commit()
            print(f"Artist '{name}' renamed to '{new_name}'.")
            break
    elif t.lower() == "song":
        song = input("Song name to modify: ").strip()
        mycursor.execute("SELECT id, songname, artistid FROM song WHERE songname = %s", (song,))
        sdata = mycursor.fetchone()
        if not sdata:
            print("Song not found.")
            break
        song_id, old_name, artist_id = sdata
        print(f"Editing song: {old_name}")
        new_song_name = input("Enter new song name (or press Enter to keep current): ").strip()
        new_artist_name = input("Enter new artist name (or press Enter to keep current): ").strip()
        if new_song_name:
            mycursor.execute("UPDATE song SET songname = %s WHERE id = %s", (new_song_name, song_id))
            mydb.commit()
            print(f"Song renamed to '{new_song_name}'")
        if new_artist_name:
            mycursor.execute("SELECT id FROM artist WHERE artistname = %s", (new_artist_name,))
            artist = mycursor.fetchone()
            if not artist:
                print(f"Artist '{new_artist_name}' not found.")
                create = input("Create this artist? (y/n): ").strip().lower()
                if create == "y":
                    mycursor.execute("INSERT INTO artist (artistname) VALUES (%s)", (new_artist_name,))
                    mydb.commit()
                    new_artist_id = mycursor.lastrowid
                    print(f"Created new artist '{new_artist_name}'")
                    break
                else:
                    print("Artist change cancelled.")
                    break
            else:
                new_artist_id = artist[0]
            mycursor.execute("UPDATE song SET artistid = %s WHERE id = %s", (new_artist_id, song_id))
            mydb.commit()
            print(f"Updated artist for song '{new_song_name or old_name}' → '{new_artist_name}'")
            break

def deletionhandler(mycursor, mydb, db):
  while True:
    print(
            "\nDeletion Menu Options:" \
            "\nDelete specific data - 1" \
            "\nWipe all data (clear all tables) - 2" \
            "\nDelete database - 3" \
            "\nExit - 4"
        )
    key = readchar.readkey()
    if key.isdigit():
      key = int(key)
      match key:
        case 1:
          print(f"\nYou chose option: {key}\n")
          t = tselector(mycursor)
          print(f"\nSelected table: {t}")
          mycursor.execute(f"SELECT * FROM {t} LIMIT 0")
          dc = [cl[0] for cl in mycursor.description]
          if "id" in dc:
            dc.remove("id")
          print("Categories:", dc)
          c = input("Which category to search from: ")
          sql = f"SELECT {c} FROM {t};"
          mycursor.execute(sql)
          res = mycursor.fetchall()
          for x in res:
            print(x)
          v = input(f"Value for '{c}' to delete: ").strip()
          if t.lower() == "artist":
              mycursor.execute("SELECT id FROM artist WHERE artistname = %s OR id = %s", (v, v))
              artist_data = mycursor.fetchone()
              if not artist_data:
                  print("Artist not found.")
                  return
              aid = artist_data[0]
              mycursor.execute("SELECT COUNT(*) FROM song WHERE artistid = %s", (aid,))
              song_count = mycursor.fetchone()[0]
              if song_count > 0:
                  print(f"\nArtist has {song_count} linked song(s)." \
                        "\nDelete the artist AND all their songs - 1" \
                        "\nKeep the songs but set their artist to 'Unknown' - 2" \
                        "\nCancel - 3"
                        )
                  key = readchar.readkey()
                  if key.isdigit():
                    key = int(key)
                    match key:
                      case 1:
                        mycursor.execute("DELETE FROM song WHERE artistid = %s", (aid,))
                        mycursor.execute("DELETE FROM artist WHERE id = %s", (aid,))
                        mydb.commit()
                        print(f"Artist and linked songs deleted.")
                      case 2:
                        mycursor.execute("SELECT id FROM artist WHERE artistname = 'Unknown'")
                        unknown = mycursor.fetchone()
                        if not unknown:
                            mycursor.execute("INSERT INTO artist (artistname) VALUES ('Unknown')")
                            mydb.commit()
                            uid = mycursor.lastrowid
                            print("Created fallback artist: 'Unknown'")
                        else:
                            uid = unknown[0]
                        mycursor.execute("UPDATE song SET artistid = %s WHERE artistid = %s", (uid, aid))
                        mycursor.execute("DELETE FROM artist WHERE id = %s", (aid,))
                        mydb.commit()
                        print("Reassigned songs to 'Unknown' and deleted artist.")
                      case _:
                        print("Action cancelled.")
                        break
              else:
                  mycursor.execute("DELETE FROM artist WHERE id = %s OR artistname = %s", (v, v))
                  mydb.commit()
                  print(f"Artist '{v}' deleted successfully.")
          elif t.lower() == "song":
              mycursor.execute(f"SELECT id, songname FROM song WHERE {c} = %s", (v,))
              sd = mycursor.fetchone()
              if not sd:
                  print("Song not found.")
                  return
              confirm = input(f"Are you sure you want to delete song '{sd[1]}'? (y/n): ").lower()
              if confirm == "y":
                  mycursor.execute("DELETE FROM song WHERE id = %s", (sd[0],))
                  mydb.commit()
                  print(f"Deleted song '{sd[1]}'.")
              else:
                  print("Action cancelled.")
          else:
              confirm = input(f"Are you sure you want to delete from '{t}' where '{c}' = '{v}'? (y/n): ").lower()
              if confirm == "y":
                  sql = f"DELETE FROM {t} WHERE {c} = %s"
                  mycursor.execute(sql, (v,))
                  mydb.commit()
                  print("Entry deleted successfully.")
                  break
              else:
                  print("Action cancelled.")
        case 2:
          print(f"\nYou chose option: {key}\n")
          mycursor.execute("SHOW TABLES")
          tables = [x[0] for x in mycursor]
          confirm = input(f"Are you sure you want to DELETE ALL TABLE DATA PERMANENTLY? y/n: ").lower()
          if confirm == "y":
            for i, t in enumerate(reversed(tables)):
              print(f"Wiping data from {t}...")
              mycursor.execute(f"DELETE FROM {t}")
              mycursor.execute(f"ALTER TABLE {t} AUTO_INCREMENT = 1")
              mydb.commit()
              print(f"Data wiped from: '{t}'.")
            break
          else:
              print("Wipe cancelled.")
        case 3:
              print(f"\nYou chose option: {key}\n")
              inp = input("Delete database y/n: ").lower()
              if inp == "y":
                print("\nDeleting the databse will remove all data permanently, \nand will result in this file closing due to the database's disappearance.")
                inp = input("Type DELETE to continue: ")
                if inp == "DELETE":
                  print("\nDeleting database...")
                  mycursor.execute(f"DROP DATABASE {db}")
                  mydb.commit()
                  break
        case 4:
              print(f"\nYou chose option: {key}\n")
              print("Exiting deletion menu...")
              mydb.close()
              break
        case _:
          print(f"\n{key} is not allowed. Try again.\n")
    else:
        print(f"\n{key} is not allowed. Try again.\n")

def nummen(mycursor, mydb, db):
  while True:
      print(
          "\nMusicRegister Menu Options:" \
          "\nWrite the corresponding number to a action to select it." \
          "\nAdd content - 1" \
          "\nView content - 2" \
          "\nUpdate/alter content - 3" \
          "\nDeletion options - 4" \
          "\nExit - 5" 
            )
      key = readchar.readkey()
      if key.isdigit():
        key = int(key)
        match key:
            case 1:
                print(f"\nYou chose option: {key}\n")
                insert(mycursor, mydb)
            case 2:
                print(f"\nYou chose option: {key}\n")
                t = tselector(mycursor)
                spesifikk(mycursor, t)
            case 3:
                print(f"\nYou chose option: {key}\n")
                t = tselector(mycursor)
                alter(mycursor, mydb, t)
            case 4:
                deletionhandler(mycursor, mydb, db)
                break
            case 5:
                print(f"\nYou chose option: {key}\n")
                print("Exiting programm...")
                break
            case _:
              print(f"\n{key} is not allowed. Try again.\n")
      else:
          print(f"\n{key} is not allowed. Try again.\n")
```
