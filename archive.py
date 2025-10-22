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