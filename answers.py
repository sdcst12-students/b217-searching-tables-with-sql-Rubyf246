'''
Assignment:

Answer the following questions about NPC's from the database. They are stored in a table called _npc_

What is the structure of the table?  What are the columns and what datatypes do they store?

[(0, 'id', 'INTEGER', 0, None, 1),
(1, 'strength', 'tinyint', 0, None, 0),
(2, 'intelligence', 'tinyint', 0, None, 0),
(3, 'wisdom', 'tinyint', 0, None, 0),
(4, 'dexterity', 'tinyint', 0, None, 0),
(5, 'constitution', 'tinyint', 0, None, 0),
(6, 'charisma', 'tinyint', 0, None, 0), 
(7, 'class', 'tinytext', 0, None, 0),
(8, 'level', 'tinyint', 0, None, 0),
(9, 'hp', 'tinyint', 0, None, 0), 
(10,'gold', 'tinyint', 0, None, 0)]

How many records are in the table?
10,000 records

How many Knights are in the table?
780 knights

Which class has the highest number of members?
[(794,)] is Thief

What is the ID number of the Jester with the most gold?

What is the total gold of the 100 wealthiest npc's in the table?

What is the total gold of the 100 wealthiest npc's under level 5?

What is the stats of the Bard with the highest strength?

What is the ID number of the npc with highest total sum of their 6 primary stats?

What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?

What is the average hitpoints per level of the npc's that are level 10 or higher?

'''
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
print(connection)

cursor = connection.cursor()
query = "Pragma table_info (npc);"
cursor.execute(query)

##query = "SELECT COUNT(*) FROM npc"
##cursor.execute(query)

##query = "SELECT COUNT(*) from npc where class= 'Knight'"
##cursor.execute(query)

#query = "select class from npc"

##query = "SELECT COUNT(*) from npc where class= 'Knight'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Knight")
##
##query = "SELECT COUNT(*) from npc where class= 'Monk'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Monk")
##
##query = "SELECT COUNT(*) from npc where class= 'Assassin'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Assassin")
##
##query = "SELECT COUNT(*) from npc where class= 'Sorcerer'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Sorcerer")
##
##query = "SELECT COUNT(*) from npc where class= 'Ranger'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Ranger")
##
##query = "SELECT COUNT(*) from npc where class= 'Priest'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Priest")
##
##query = "SELECT COUNT(*) from npc where class= 'Samurai'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Samurai")
##
##query = "SELECT COUNT(*) from npc where class= 'Barbarian'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Barbarian")
##
##query = "SELECT COUNT(*) from npc where class= 'Bard'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Bard")
##
##query = "SELECT COUNT(*) from npc where class= 'Thief'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Thief")
##
##query = "SELECT COUNT(*) from npc where class= 'Warrior'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Warrior")
##
##query = "SELECT COUNT(*) from npc where class= 'Jester'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Jester")
##
##query = "SELECT COUNT(*) from npc where class= 'Sage'"
##cursor.execute(query)
##results = cursor.fetchall ()
##print(f"{results} is Sage")
##

query = "SELECT * from npc ORDER BY gold ASC;"
cursor.execute(query)



results = cursor.fetchall ()
print(results)
