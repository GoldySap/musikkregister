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
  inp = input("Insert test values? y/n ")
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
          artist_map = {name.lower(): artist_id for artist_id, name in mycursor.fetchall()}
          sints = []
          for artistname, songname in val:
              artist_id = artist_map.get(artistname.lower())
              if artist_id:
                  sints.append((songname, artist_id))
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
    mycursor.execute("SHOW TABLES")
    temp = [x[0] for x in mycursor]
    while True:
        vs = []
        print("\nAvalible tables:")
        for i, string in enumerate(temp):
            print(f"{string} - {i + 1}")
            vs.append((i + 1, string))
        key = readchar.readkey()
        if key.isdigit():
            key = int(key)
            for number, string in vs:
                if key == number:
                    t = string.lower()
                    print(f"\nSelected tabel: {t}")
                    if t == "artist":
                        count = int(input("How many artist to add: "))
                        for _ in range(count):
                            aname = input("Artistname: ")
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
                            sname = input("Songname: ")
                            aname = input("Artistname: ")
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
                    else:
                        print("Unkown tabel.")
                    return
            print(f"'{key}' is not allowed. Try again.")
        else:
            print(f"'{key}' is not allowed. Try again.")

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
        if key.isdigit():
          key = int(key)
          for number, string in vs:
            if key == number:
              return string
        else:
            print(f"{key} is not allowed. Try again:")

def spesifikk(mycursor, t):
  while True:
      print(
      "\nSearch Options:" \
      "\nView all content - 1" \
      "\nSearch category content - 2" \
      "\nSearch spesifikk content - 3"
        )
      allowed_keys = {1, 2, 3}
      key = int(readchar.readkey())
      if key in allowed_keys:
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
                  sql = f"SELECT * FROM {t} WHERE {c} ='{o}'"
                  mycursor.execute(sql)
                  res = mycursor.fetchall()
                  for x in res:
                    print(x)
                  cres = list({row["artist"] for row in t})
                  print("artists:", cres)
                  o = input("What to search for in the category: ")
                  if c.lower in dc:
                    sql = f"SELECT * FROM {t} WHERE {c} ='{o}'"
                    mycursor.execute(sql)
                    res = mycursor.fetchall()
                    for x in res:
                        print(x)
                  else:
                    print("Invalid search category.")
                    spesifikk(t)
                  break
      else:
        print(f"\n{key} is not allowed. Try again.\n")

def alter(mycursor, mydb, t):
    mycursor.execute(f"SELECT * FROM {t} LIMIT 0")
    dc = [cl[0] for cl in mycursor.description]
    if "id" in dc:
      dc.remove("id")
    print("Categories:", dc)
    c = input("Which category to search from: ")
    sql = f"SELECT * FROM {t} WHERE {c} ='{o}'"
    mycursor.execute(sql)
    res = mycursor.fetchall()
    for x in res:
      print(x)
    cres = list({row["artist"] for row in t})
    print("artists:", cres)
    o = input("What to search for in the category: ")
    if c.lower in dc:
      sql = f"SELECT * FROM {t} WHERE {c} ='{o}'"
      mycursor.execute(sql)
      res = mycursor.fetchall()
      for x in res:
          print(x)
    sql = f"UPDATE {t} SET address = %s WHERE address = %s"
    val = []
    mycursor.execute(sql, val)
    dc = [cl[0] for cl in mycursor.description]
    an = input("What to change: ")
    na = input("New content values: ")
    mycursor.execute(f"SELECT {an} FROM {t} WHERE id = %s", (an))
    og = mycursor.fetchone()
    sql = f"UPDATE {t} SET {t} = %s WHERE id = %s"
    mycursor.execute(sql, (na, an))
    mydb.commit()
    mycursor.execute("UPDATE Music set Artist = %s WHERE Artist = %s", (an, og[0],))
    mydb.commit()

def deletionhandler(mycursor, mydb, db):
  while True:
    print(
            "\nDeletion Menu Options:"
            "\nDelete specific data - 1"
            "\nWipe all data (clear all tables) - 2"
            "\nDelete database - 3"
            "\nExit - 4"
        )
    allowed_keys = {1, 2, 3, 4}
    key = int(readchar.readkey())
    if key in allowed_keys:
      match key:
        case 1:
          print(f"\nYou chose option: {key}\n")
          mycursor.execute("SHOW TABLES")
          tables = [x[0] for x in mycursor]
          print("\nAvailable tables:")
          for i, table in enumerate(tables):
            print(f"{i + 1}. {table}")
          t_choice = input("Select table number: ").strip()
          if not t_choice.isdigit() or int(t_choice) not in range(1, len(tables) + 1):
            print("Invalid table choice.")
            return
          t = tables[int(t_choice) - 1]
          print(f"\nSelected table: {t}")
          mycursor.execute(f"SELECT * FROM {t} LIMIT 0")
          columns = [col[0] for col in mycursor.description]
          print("Available columns:", columns)
          c = input("Which column to search by (e.g., 'id' or 'artistname'): ").strip()
          if c not in columns:
              print("Invalid column.")
              return
          v = input(f"Enter value for '{c}' to delete: ").strip()
          if t.lower() == "artist":
              mycursor.execute("SELECT id FROM artist WHERE artistname = %s OR id = %s", (v, v))
              artist_data = mycursor.fetchone()
              if not artist_data:
                  print("Artist not found.")
                  return
              artist_id = artist_data[0]
              mycursor.execute("SELECT COUNT(*) FROM song WHERE artistid = %s", (artist_id,))
              song_count = mycursor.fetchone()[0]
              if song_count > 0:
                  print(f"\nArtist has {song_count} linked song(s).")
                  print("Delete the artist AND all their songs - 1")
                  print("Keep the songs but set their artist to 'Unknown' - 2")
                  print("Cancel - 3")
                  allowed_keys = {1, 2, 3}
                  key = int(readchar.readkey())
                  if key in allowed_keys:
                    match key:
                      case 1:
                        mycursor.execute("DELETE FROM song WHERE artistid = %s", (artist_id,))
                        mycursor.execute("DELETE FROM artist WHERE id = %s", (artist_id,))
                        mydb.commit()
                        print(f"Deleted artist and all linked songs.")
                      case 2:
                        mycursor.execute("SELECT id FROM artist WHERE artistname = 'Unknown'")
                        unknown = mycursor.fetchone()
                        if not unknown:
                            mycursor.execute("INSERT INTO artist (artistname) VALUES ('Unknown')")
                            mydb.commit()
                            unknown_id = mycursor.lastrowid
                            print("Created fallback artist: 'Unknown'")
                        else:
                            unknown_id = unknown[0]
                        mycursor.execute("UPDATE song SET artistid = %s WHERE artistid = %s", (unknown_id, artist_id))
                        mycursor.execute("DELETE FROM artist WHERE id = %s", (artist_id,))
                        mydb.commit()
                        print("Reassigned songs to 'Unknown' and deleted artist.")
                      case _:
                        print("Action cancelled.")
                        return
              else:
                  mycursor.execute("DELETE FROM artist WHERE id = %s OR artistname = %s", (v, v))
                  mydb.commit()
                  print(f"Artist '{v}' deleted successfully.")
          elif t.lower() == "song":
              mycursor.execute(f"SELECT id, songname FROM song WHERE {c} = %s", (v,))
              song_data = mycursor.fetchone()
              if not song_data:
                  print("Song not found.")
                  return
              confirm = input(f"Are you sure you want to delete song '{song_data[1]}'? (y/n): ").lower()
              if confirm == "y":
                  mycursor.execute("DELETE FROM song WHERE id = %s", (song_data[0],))
                  mydb.commit()
                  print(f"Deleted song '{song_data[1]}'.")
              else:
                  print("Action cancelled.")
          else:
              confirm = input(f"Are you sure you want to delete from '{t}' where '{c}' = '{v}'? (y/n): ").lower()
              if confirm == "y":
                  sql = f"DELETE FROM {t} WHERE {c} = %s"
                  mycursor.execute(sql, (v,))
                  mydb.commit()
                  print("Entry deleted successfully.")
              else:
                  print("Action cancelled.")
        case 2:
          print(f"\nYou chose option: {key}\n")
          mycursor.execute("SHOW TABLES")
          tables = [x[0] for x in mycursor]
          print("\nAvailable tables:")
          for i, table in enumerate(tables):
              print(f"{i + 1}. {table}")
          t_choice = input("Select table number to wipe: ").strip()
          if not t_choice.isdigit() or int(t_choice) not in range(1, len(tables) + 1):
              print("Invalid table choice.")
              return
          t = tables[int(t_choice) - 1]
          confirm = input(f"Are you sure you want to DELETE ALL DATA from '{t}'? y/n: ").lower()
          if confirm == "y":
              mycursor.execute(f"DELETE FROM {t}")
              mycursor.execute(f"ALTER TABLE {t} AUTO_INCREMENT = 1")
              mydb.commit()
              print(f"Data wiped from: '{t}'.")
          else:
              print("Wipe cancelled.")
        case 3:
              print(f"\nYou chose option: {key}\n")
              inp = input("Delete database y/n: ").lower()
              if inp == "y":
                print("\nDeleting the databse will remove all data permanently, \nand will result in this file crashing due to losing connection.")
                inp = input("Type DELETE to continue: ")
                if inp == "DELETE":
                  print("\nDeleting database...")
                  mycursor.execute(f"DROP DATABASE {db}")
                  mydb.commit()
                  break
        case 4:
              print(f"\nYou chose option: {key}\n")
              print("Exiting deletion menu...")
              break
    else:
        print(f"\n{key} is not allowed. Try again.\n")

def nummen(mycursor, mydb, db):
  while True:
      print(
          "\nMusicRegister Menu Options:" \
          "\nAdd content - 1" \
          "\nView content - 2" \
          "\nUpdate/alter content - 3" \
          "\nDeletion options - 4" \
          "\nExit - 5" 
            )
      allowed_keys = {1, 2, 3, 4, 5}
      key = int(readchar.readkey())
      if key in allowed_keys:
          match key:
              case 1:
                  print(f"\nYou chose option: {key}\n")
                  insert(mycursor, mydb)
              case 2:
                  print(f"\nYou chose option: {key}\n")
                  t = viewer(mycursor)
                  spesifikk(mycursor, t)
              case 3:
                  print(f"\nYou chose option: {key}\n")
                  t = viewer()
                  alter(mycursor, mydb, t)
              case 4:
                  deletionhandler(mycursor, mydb, db)
                  break
              case 5:
                  print(f"\nYou chose option: {key}\n")
                  break
      else:
          print(f"\n{key} is not allowed. Try again.\n")