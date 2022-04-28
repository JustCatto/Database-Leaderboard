import sqlite3
import os.path as os

if os.isfile("Test.db") == False:
    database = sqlite3.connect("Test.db")
    cursor = database.cursor()
    cursor.execute("""CREATE TABLE Cats 
        (KittenID INTEGER PRIMARY KEY NOT NULL,
        CatType VARCHAR(20),
        CatAge INTEGER)""")
else:
    database = sqlite3.connect("Test.db")
    cursor = database.cursor()

#IntegrityError occurs
cursor.execute("""INSERT INTO Cats(KittenID,CatType,CatAge) VALUES (69,"Tabby",69)""")
cursor.execute("""INSERT INTO Cats(KittenID,CatType,CatAge) VALUES (69,"Ginger",50)""")
cursor.commit()