import unittest
import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'accounts', password = 'Elite102Code2College@987')
cursor = connection.cursor()


def menuScreen():	
	print("-----------------------------------------------------------")
	print("---------------------CODE2COLLEGE BANK---------------------")
	print("-----------------------------------------------------------")
	print()

	name = input("What is your name? >>> ")
  	
	print()
	name = name.capitalize()
	print(f"Welcome {name}! We're happy to see you here.")

	print()
	
	print("------------------------------")
	print("1. Create an Account")
	print("2. Login")
	print("------------------------------")


	selection = input("Please select what you would like to do: ")
	if((isinstance(selection, int)) and (int(selection) > 2 or int(selection) <= 0)): #if it's not one or two
		print("INVALID INPUT")
		return
	

	if(int(selection) == 1):
		password = input("What would you like your password to be? >>> ")
		email = input("What is your email? >>> ")
		createNewAccount(email, name, password, 0.0)
	elif(int(selection) == 2):
		email = input("What is your email? >>> ")
		password = input("What is your password? >>> ")
		print()
		print("---------------------------")
		print("1. View Funds")
		print("2. Deposit Funds")
		print("3. Withdraw Funds")
		print("4. Modify Account Details")
		print("5. Delete Account")
		print("---------------------------")
		option = input("Select an action >>> ")

		if((isinstance(option, int)) and (int(option) > 5 or int(option) < 1)):
			print("INVALID INPUT")
			return

		if(int(option) == 1):
			checkAccountBalance(email)
		elif(int(option) == 2):
			amountDeposit = input("How many funds? >>> ")
			depositFunds(email, float(amountDeposit))
		elif(int(option) == 3):
			amountWithDraw = input("How many funds? >>> ")
			withdrawFunds(email, float(amountWithDraw))
		elif(int(option) == 4):
			print("1. Name")
			print("2. Password")
			print("3. Email")

			option = input("What would you like to modify? >>> ")
			value = input("What would you like to change it to? >>> ")

			if(option == 1):
				modifyAccountDetails(email, value, "name")
			elif(option == 2):
				modifyAccountDetails(email, value, "password")
			elif(option == 3):
				modifyAccountDetails(email, value, "email")
			else:
				print("INVALID INPUT")
				return

		elif(selection == 5):
			option = input("Are you sure you want to delete your account? All your data, including your money, will be wiped from our system.")
			if(option.lower() == 'yes' or option.lower() == 'y'):
				deleteAccount(email)

#def inputValidation():
#	pass


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
	balance = cursor.fetchall()

	print(f"TROUBLESHOOTING: BALANCE IS {balance[0][0]}.")

	updateFundsQuery = (f"UPDATE accounts SET Balance = {float(balance[0][0]) + amountToDeposit} WHERE Email = '{email}';") #get the deposit
	cursor.execute(updateFundsQuery)

	checkAccountBalance(email)

	

		
	#if(cursor.fetchone()[0] <= 0):
	#	print("EMAIL NOT FOUND")
	#	return False

	#newBalance = cursor + amountToDeposit

	#addNewBalanceQuery = (f"INSERT INTO accounts(Email, Balance) VALUES('{email}', {newBalance});")
	#cursor.execute(addNewBalanceQuery)

	return True
	

def withdrawFunds(email, amountToWithdraw):
	#first, get the balance in the account
	viewAccountBalanceQuery = (f"SELECT Balance FROM accounts WHERE Email = '{email}';")
	cursor.execute(viewAccountBalanceQuery)

	total = 0
	for item in cursor:
		total += float(item)

	#update the balance (if it's over the amount to withdraw)
	if(total < amountToWithdraw):
		print("NOT ENOUGH FUNDS")
		return False
	else:
		updateFundsQuery = (f"UPDATE accounts SET Balance = {total-amountToWithdraw} WHERE Email = '{email}';") #get the deposit
		cursor.execute(updateFundsQuery)
		checkAccountBalance(email)


	"""
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
	"""

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
	#three things that can be changed: email, name, and password
 
	if(columnToChange.lower() == 'email'):
		changeRequest = (f"UPDATE accounts SET Email = '{value}' WHERE Email = '{email}';")
	elif(columnToChange.lower() == 'name'):
		changeRequest = (f"UPDATE accounts SET Name = '{value}' WHERE Email = '{email}';")
	elif(columnToChange.lower() == 'password'):
		changeRequest = (f"UPDATE accounts SET Password = '{value}' WHERE Email = '{email}';")
	else:
		print("INVALID INPUT.")
		return False
	
	cursor.execute(changeRequest)

	viewAccountDetails()
	
	"""
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
	"""
	

def viewAccountDetails(email):
	viewAccountDetailsQuery = (f"SELECT * FROM accounts WHERE Email = '{email}'") #get the information from the table
	cursor.execute(viewAccountDetailsQuery)

	print("YOUR ACCOUNT DETAILS") #print data
	for item in cursor:
		print(item)
		print('\n')

	return True #attests that the function went off without a hitch


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

#test = input("enter a letter >>> ")
menuScreen()
#print(test)

print()

cursor.close()
connection.close()