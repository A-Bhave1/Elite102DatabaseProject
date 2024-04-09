import unittest
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

	if(cursor.fetchone()[0] <= 0):
		print("EMAIL NOT FOUND")
		return False

	print(f"YOUR ACCOUNT DETAILS:")
	for item in cursor:
		print(item)

	return True

def depositFunds(email, amountToDeposit):
	getBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = {email};") #get the deposit
	cursor.execute(getBalanceQuery)

	if(cursor.fetchone()[0] <= 0):
		print("EMAIL NOT FOUND")
		return False

	newBalance = cursor + amountToDeposit

	addNewBalanceQuery = (f"INSERT INTO accounts(Email, Balance) VALUES({email}, {newBalance});")
	cursor.execute(addNewBalanceQuery)

	return True
	

def withdrawFunds(email, amountToWithdraw):
	getBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = {email};") #get the deposit
	cursor.execute(getBalanceQuery)

	if(cursor.fetchone()[0] <= 0):
		print("EMAIL NOT FOUND")
		return False

	newBalance = cursor - amountToWithdraw
	if(newBalance < 0):
		print("NOT SUFFICIENT FUNDS.")
		return False

	addNewBalanceQuery = (f"INSERT INTO accounts(Email, Balance) VALUES({email}, {newBalance});")
	cursor.execute(addNewBalanceQuery)
	return True

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
	return True

def deleteAccount(email):
	getDeleteQuery = (f"SELECT Email FROM accounts WHERE Email = {email};") 
	cursor.execute(getDeleteQuery)
	
	if(cursor.fetchone()[0] <= 0):
		print("EMAIL NOT FOUND")
		return False
	
	deleteCommand = (f"DELETE FROM accounts WHERE Email = {email};")
	cursor.execute(deleteCommand)

	return True

def modifyAccountDetails(email, value, columnToChange):
	if(columnToChange.lower() == "email"):
		changeEmail = (f"INSERT INTO accounts(Email) VALUES({value});")
		cursor.execute(changeEmail)
		if(cursor.fetchone()[0] <= 0):
			print("EMAIL NOT FOUND")
			return False
		return True

	elif(columnToChange.lower() == "name"):
		changeName = (f"INSERT INTO accounts(Email, Name) VALUES({email}, {value});")
		cursor.execute(changeName)
		if(cursor.fetchone()[0] <= 0):
			print("EMAIL NOT FOUND")
			return False
		return True
		
	elif(columnToChange.lower() == "password"):
		changePassword = (f"INSERT INTO accounts(Email, Password) VALUES({email}, {value});")
		cursor.execute(changePassword)
		if(cursor.fetchone()[0] <= 0):
			print("EMAIL NOT FOUND")
			return False
		return True
	else:
		print("INVALID INPUT.")
		return False



class testApplication(unittest.TestCase):
	
	def testCREATENEWACCOUNT(self):
		result = createNewAccount("anushkabhave8@gmail.com", "Test@123", "Anushka Bhave", 1.00)
		testApplication.assertTrue(result)

