import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'example', password = 'Elite102Code2College@987')
cursor = connection.cursor()

addData = ("INSERT INTO example.inventory(ID, NameOfItem, Price, CategoryOfItem, DateCreated, NumberSold) VALUES (3, 'Gift Bags', 1.00, 'Party Goods', '2024-04-01', 20);")

cursor.execute(addData)

testQuery = ("SELECT * FROM example.inventory")
cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()
connection.close()



def menuScreen():
	print("-----------------------------------------------------------")
	print("--------------------DATABASING PROJECT --------------------")
	print("-----------------------------------------------------------")
	print()

	name = input("What is your name? >>> ")
	print()
	name = name.capitalize()
	print(f"Welcome {name}! We're happy to see you here.")

#menuScreen()