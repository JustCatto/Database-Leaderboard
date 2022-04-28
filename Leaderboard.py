#Leaderboard code for magder

import random
import sqlite3
import os.path as os
leaderboardDatabase = "Leaderboard.db"

class Database:
    def __init__(self):
        if self._checkIfSQLDB(leaderboardDatabase) != True:
            self.database = sqlite3.connect(leaderboardDatabase)
            self._initialiseDatabase()
        else:
            self.database = sqlite3.connect(leaderboardDatabase)

    def _initialiseDatabase(self):
        databaseCursor = self.database.cursor()
        databaseCursor.execute("""
        CREATE TABLE Leaderboard(
            GameID INTEGER PRIMARY KEY NOT NULL,
            PlayerName VARCHAR(5) NOT NULL,
            Time INTEGER NOT NULL
        )
        """)
        databaseCursor.close()
        self.database.commit()

    def _checkIfSQLDB(self,fileName):
        if not os.isfile(fileName):
            print("File does not exist")
            return False
        if os.getsize(fileName) < 100:
            print("File is not large enough to be a db")
            return False
        with open(fileName,"rb") as file:
            header = file.read(100)
        return header[:16] == b'SQLite format 3\x00'

    def appendToLeaderboard(self,Name,Time):
        databaseCursor = self.database.cursor()
        while True:
            try:
                gameID = random.randint(0,999999)
                databaseCursor.execute("INSERT INTO Leaderboard VALUES(?,?,?);",(gameID,Name,Time))
            except sqlite3.IntegrityError:
                pass
            else:
                databaseCursor.close()
                self.database.commit()
                break
    
    def readLeaderboard(self):
        databaseCursor = self.database.cursor()
        databaseCursor.execute("SELECT * FROM Leaderboard;")
        Data = databaseCursor.fetchall()
        print(Data)
        databaseCursor.close()

    def deleteFromLeaderboard(self,ID):
        databaseCursor = self.database.cursor()
        databaseCursor.execute("DELETE FROM Leaderboard WHERE GameID=?",(ID,))
        databaseCursor.close()
        self.database.commit()


#Test lines to check if DB works
Leaderboard = Database()
Leaderboard.readLeaderboard()
ID = int(input("-->"))
Leaderboard.deleteFromLeaderboard(ID)
Leaderboard.readLeaderboard()
