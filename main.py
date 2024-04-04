import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'example', password = 'Elite102Code2College@987')
cursor = connection.cursor()

#addData = ("INSERT INTO example.inventory(ID, NameOfItem, Price, CategoryOfItem, DateCreated, NumberSold) VALUES (3, 'Gift Bags', 1.00, 'Party Goods', '2024-04-01', 20);")

#cursor.execute(addData)

#testQuery = ("SELECT * FROM example.inventory")
#cursor.execute(testQuery)

#for item in cursor:
 #   print(item)

#cursor.close()
#connection.close()


def menuScreen():	
	print("-----------------------------------------------------------")
	print("--------------------DATABASING PROJECT --------------------")
	print("-----------------------------------------------------------")
	print()

	name = input("What is your name? >>> ")
	print()
	name = name.capitalize()
	print(f"Welcome {name}! We're happy to see you here.")

def checkAccountBalance(email):
	accountBalanceQuery = (f"SELECT * FROM accounts WHERE Email = {email};")
	cursor.execute(accountBalanceQuery)

	print(f"YOUR ACCOUNT DETAILS:")
	for item in cursor:
		print(item)

def depositFunds(email, amountToDeposit):
	getBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = {email};") #get the deposit
	cursor.execute(getBalanceQuery)
	newBalance = cursor + amountToDeposit

	addNewBalanceQuery = (f"INSERT INTO accounts(Email, Balance) VALUES({email}, {newBalance});")
	cursor.execute(addNewBalanceQuery)
	

def withdrawFunds(email, amountToWithdraw):
	getBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = {email};") #get the deposit
	cursor.execute(getBalanceQuery)
	newBalance = cursor - amountToWithdraw
	if(newBalance < 0):
		print("NOT SUFFICIENT FUNDS.")
		return

	addNewBalanceQuery = (f"INSERT INTO accounts(Email, Balance) VALUES({email}, {newBalance});")
	cursor.execute(addNewBalanceQuery)

def createNewAccount(email, password, name, balance):
	print("THANK YOU. PROCESSING...")

	createAccount = (f"INSERT INTO accounts(Name, Email, Password, Balance) VALUES({name},{email},{password},{balance});")
	cursor.execute(createAccount)

	print("YOUR ACCOUNT INFORMATION:")
	viewNewAccountInfo = (f"SELECT * FROM accounts WHERE Email = {email};")
	cursor.execute(viewNewAccountInfo)
	for item in cursor:
		print(item)
	print("IF ANYTHING IS INCORRECT, PLEASE DON'T HESITATE TO CHANGE YOUR ACCOUNT DETAILS.")

def deleteAccount(email):
	pass

def modifyAccountDetails(email, value, columnToChange):
	if(columnToChange.lower() == "email"):
		changeEmail = (f"INSERT INTO accounts(Email) VALUES({value});")
		cursor.execute(changeEmail)

	elif(columnToChange.lower() == "name"):
		changeName = (f"INSERT INTO accounts(Email, Name) VALUES({email}, {value});")
		cursor.execute(changeName)
		
	elif(columnToChange.lower() == "password"):
		changePassword = (f"INSERT INTO accounts(Email, Password) VALUES({email}, {value});")
		cursor.execute(changePassword)

	else:
		print("INVALID INPUT.")


