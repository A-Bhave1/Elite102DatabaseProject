import unittest
import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'accounts', password = 'Elite102Code2College@987')
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
	print("---------------------CODE2COLLEGE BANK---------------------")
	print("-----------------------------------------------------------")
	print()

	name = input("What is your name? >>> ")
	email = input("What is your email? >>> ")
	print()
	name = name.capitalize()
	print(f"Welcome {name}! We're happy to see you here.")

	print()
	
	print("1. Create an Account")
	print("2. Login")

	input = input("Please select what you would like to do:")
	if(input == 1):
		password = input("What would you like your password to be? >>> ")
		createNewAccount(email, name, password, 0.0)
	elif(input == 2):
		password = input("What is your password? >>> ")
		print()
		print("1. Deposit Funds")
		print("2. Withdraw Funds")
		option = input("Select an action >>> ")
		if(option == 1):
			amountDeposit = input("How many funds? >>> ")
			depositFunds(email, float(amountDeposit))
		elif(option == 2):
			amountWithDraw = input("How many funds? >>> ")
			withdrawFunds(email, float(amountWithDraw))



def checkAccountBalance(email):
	print()
	accountBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = '{email}';")
	cursor.execute(accountBalanceQuery)
	#row = cursor.fetchone(accountBalanceQuery)

	#if(row is None):
	#	print("EMAIL NOT FOUND")
	#	return False

	print(f"YOUR ACCOUNT DETAILS:")
	for item in cursor:
		print(item)

	return True

def depositFunds(email, amountToDeposit): #THIS IS FUNDAMENTALLY FLAWED?
	accountBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = '{email}';")
	cursor.execute(accountBalanceQuery)

	total = amountToDeposit
	for item in cursor:
		total += float(item)

	updateFundsQuery = (f"UPDATE accounts SET Balance = {total} WHERE Email = '{email}';") #get the deposit
	cursor.execute(updateFundsQuery)

	

		
	#if(cursor.fetchone()[0] <= 0):
	#	print("EMAIL NOT FOUND")
	#	return False

	#newBalance = cursor + amountToDeposit

	#addNewBalanceQuery = (f"INSERT INTO accounts(Email, Balance) VALUES('{email}', {newBalance});")
	#cursor.execute(addNewBalanceQuery)

	return True
	

def withdrawFunds(email, amountToWithdraw):
	getBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = '{email}';") #get the deposit
	cursor.execute(getBalanceQuery)

	if(cursor.fetchone()[0] <= 0):
		print("EMAIL NOT FOUND")
		return False

	newBalance = cursor - amountToWithdraw
	if(newBalance < 0):
		print("NOT SUFFICIENT FUNDS.")
		return False

	addNewBalanceQuery = (f"INSERT INTO accounts(Email, Balance) VALUES('{email}', {newBalance});")
	cursor.execute(addNewBalanceQuery)
	return True

def createNewAccount(email, password, name, balance):
	print("THANK YOU. PROCESSING...")

	#print(f"INSERT INTO accounts VALUES('{str(name)}', '{str(email)}', '{str(password)}', {float(balance)});")
	#print()
	createAccount = (f"INSERT INTO accounts VALUES('{str(name.upper())}', '{str(email.lower())}', '{str(password)}', {float(balance)});")

	cursor.execute(createAccount) #error here

	print("YOUR ACCOUNT INFORMATION:")
	viewNewAccountInfo = (f"SELECT * FROM accounts WHERE Email = '{email}';")
	cursor.execute(viewNewAccountInfo)
	for item in cursor:
		print(item)
	print("IF ANYTHING IS INCORRECT, PLEASE DON'T HESITATE TO CHANGE YOUR ACCOUNT DETAILS.")
	return True

def deleteAccount(email):
	#getDeleteQuery = (f"SELECT Email FROM accounts WHERE Email = '{email}';") 
	#cursor.execute(getDeleteQuery)
	
	#if(cursor.fetchone()[0] <= 0):
	#	print("EMAIL NOT FOUND")
	#	return False
	
	deleteCommand = (f"DELETE FROM accounts WHERE Email = '{email}';")
	cursor.execute(deleteCommand)

	print("ACCOUNT DELETED")

	return True

def modifyAccountDetails(email, value, columnToChange): #THIS IS FUNDAMENTALLY FLAWED, FIX IT!
	if(columnToChange.lower() == "email"):
		changeEmail = (f"INSERT INTO accounts(Email) VALUES('{value}');")
		cursor.execute(changeEmail)
		if(cursor.fetchone()[0] <= 0):
			print("EMAIL NOT FOUND")
			return False
		return True

	elif(columnToChange.lower() == "name"):
		changeName = (f"INSERT INTO accounts(Email, Name) VALUES('{email}', '{value}');")
		cursor.execute(changeName)
		if(cursor.fetchone()[0] <= 0):
			print("EMAIL NOT FOUND")
			return False
		return True
		
	elif(columnToChange.lower() == "password"):
		changePassword = (f"INSERT INTO accounts(Email, Password) VALUES('{email}', '{value}');")
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

	def testCHECKACCOUNTBALANCE(self):
		result = checkAccountBalance("anushkabhave8@gmail.com")
		testApplication.assertTrue(result)

	def testDEPOSITFUNDS(self):
		result = depositFunds("anushkabhave8@gmail.com", 1.00)
		testApplication.assertTrue(result)

	def testWITHDRAWFUNDS(self):
		result = withdrawFunds("anushkabhave8@gmail.com", 1.00)
		testApplication.assertTrue(result)

	def testMODIFYACCOUNTDETAILS(self):
		result = modifyAccountDetails("anushkabhave8@gmail.com", "Arin Bhave", "name")
		testApplication.assertTrue(result)

	def testDELETEACCOUNT(self):
		result = deleteAccount("anushkabhave8@")
		testApplication.assertTrue(result)

print()

#createNewAccount("anushkabhave8@gmail.com", "C2C", "Anushka Bhave", 0.0)
createNewAccount("bhave.alex@gmail.com", "C2C123", "Arin Bhave", 0.0)

checkAccountBalance("bhave.alex@gmail.com")

depositFunds("bhave.alex@gmail.com", 1.0)

checkAccountBalance("bhave.alex@gmail.com")

#deleteAccount("bhave.alex@gmail.com")

print()

cursor.close()
connection.close()