""" Universal table selection system, but not needed for the project """
"""     print("Current tables:", temp)
    print("Default table:", musikkregister.defaulttable)
    inp = input("View default table? y/n ")
    if inp.lower() == "y":
      t = musikkregister.envtables
      print("Default table selected:", t)
    else:
      t = input("Name of table: ")
      if t not in temp:
         print("Invalid table") """

""" Setts a new default by overwriting the .env variable value """
""" def defaultsett():
    musikkregister.mycursor.execute("SHOW TABLES")
    temp = [x[0] for x in musikkregister.mycursor]
    print("Current tables:", temp)
    print("Default table:", musikkregister.defaulttable)
    envpath = musikkregister.os.path.join(musikkregister.os.path.dirname(__file__), '.env')
    musikkregister.dotenv.set_key(envpath, "DEFAULTTABLE", "artist") """

""" Asks i user wants to use default database or not """
""" print("\nCurrent tables:", temp, "\nDefault table:", musikkregister.envtables)
        inp = input("Use default table? y/n ")
        if inp == "y":
          t = musikkregister.envtables
          print("Default table selected:", t)
        else:
          t = str(input("Select table to insert content: ")) """

""" Interactive Menu """
""" def show_m():
    print("\033c", end="")
    print("=== MENU ===")
    for i, option in enumerate(options):
        prefix = "> " if i == selected else "  "
        print(prefix + option)

def itrmen():
   while True:
    show_m()
    key = musikkregister.readchar.readkey()
    if key == musikkregister.readchar.key.UP:
        selected = (selected - 1) % len(options)
    elif key == musikkregister.readchar.key.DOWN:
        selected = (selected + 1) % len(options)
    elif key == "\r":
        print(f"You selected {options[selected]}")
        break """


""" test insert code """
""" mycursor.execute(f"SELECT COUNT(*) FROM {}")
      artist_count = mycursor.fetchone()[0]
       mycursor.execute(f"SELECT * FROM artist WHERE artistname = {aname};")
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
        print(mycursor.rowcount, "was inserted.") """

""" Gammel insert function """
""" def insert(mycursor, mydb):
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
            print(f"{key} is not allowed. Try again:") """