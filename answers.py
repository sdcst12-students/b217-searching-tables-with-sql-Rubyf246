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

#############################################

##query = "Pragma table_info (npc);"
##cursor.execute(query)
#############################################

How many records are in the table?
10,000 records
#############################################

##query = "SELECT COUNT(*) FROM npc"
##cursor.execute(query)
#############################################

How many Knights are in the table?
780 knights
#############################################
##query = "SELECT COUNT(*) from npc where class= 'Knight'"
##cursor.execute(query)
#############################################

Which class has the highest number of members?
[(794,)] is Thief

#############################################
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
#############################################



What is the ID number of the Jester with the most gold?
7907, 9653
(7907, 11, 13, 12, 13, 14, 9, 'Jester', 12, 50, 51)
(9653, 8, 10, 12, 10, 13, 7, 'Jester', 12, 57, 51)

##############################################
##query = "select * from npc where class = 'Jester' and gold = (select max(gold) from npc where class = 'Jester')"
############################################## 
 

What is the total gold of the 100 wealthiest npc's in the table?
4917
##############################################
query = "select sum(gold) from (select * from npc order by gold desc limit 100)"
##############################################

What is the total gold of the 100 wealthiest npc's under level 5?
4917
##############################################
query = "select sum(gold) from (select * from npc where level <5 order by gold desc limit 100)"
##############################################


What is the stats of the Bard with the highest strength?
(3672, 18, 7, 13, 8, 11, 12, 'Bard', 5, 22, 23)
##############################################
query = "select * from npc where class = 'Bard' and strength = (select max(strength) from npc where class = 'Bard')"
##############################################

What is the ID number of the npc with highest total sum of their 6 primary stats?
(2693, 89)
(8693, 89)
##############################################
# total of 6 columns
query = "select ID, (strength + intelligence + wisdom + dexterity + constitution + charisma) as total_stats from npc where strength + intelligence + wisdom + dexterity + constitution + charisma = (select max(strength + intelligence + wisdom + dexterity + constitution + charisma) from npc)"
##############################################

What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?
3048
##############################################
query = "select count(*) from npc where class in ('Barbarian', 'Warrior', 'Knight', 'Samurai')"
##############################################

What is the average hitpoints per level of the npc's that are level 10 or higher?
(4.035202863961814,)
##############################################
query = "select avg(hp/level) from npc where level >= 10"
##############################################

'''
import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)

cursor = connection.cursor()
 
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

query = "select avg(hp/level) from npc where level >= 10"
 
cursor.execute(query)
result = cursor.fetchall()
for i in result:
    print(i)
