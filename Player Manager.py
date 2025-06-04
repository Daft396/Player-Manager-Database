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

def display_interface():
    print("Welcome to the Game Character Manager")
    print("\n")
    print("1) Add Character")
    print("2) View all Characters")
    print("3) Update Character")
    print("4) Delete Character")
    print("5) Exit")
    print("\n")
    choice = int(input("Enter Your Choice: "))
    while choice != 5:
        if choice == 1:
            addchar()
        elif choice== 2:
            viewchars()
        elif choice== 3:
            upchar()
        elif choice == 4:
            delchar()
        elif choice == 5:
            print("Thanks for using our program!")
            break
def addchar():
    pass

def viewchars():
    pass

def upchar():
    pass

def delchar():
    pass
