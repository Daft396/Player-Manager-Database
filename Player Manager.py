import sqlite3
DB = sqlite3.connect('Player Manager.db')

cursor = DB.cursor()

Create = '''
CREATE TABLE IF NOT EXISTS Characters(
Id INTEGER PRIMARY KEY,
Name TEXT NOT NULL,
Class TEXT NOT NULL,
Level INTEGER NOT NULL);'''
cursor.execute(Create)
DB.commit()



