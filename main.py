import unittest
import os
import time
import mysql.connector
connection = mysql.connector.connect(user = 'root', database = 'accounts', password = 'Elite102Code2College@987')
cursor = connection.cursor()


#displays the initial menu screen
def menuScreen():	

	print("-----------------------------------------------------------")
	print("---------------------CODE2COLLEGE BANK---------------------")
	print("-----------------------------------------------------------")
	print()

	print("------------------------------")
	print("1. Create an Account")
	print("2. Login")
	print("3. Exit")
	print("------------------------------")


	selection = input("Please select what you would like to do: ")
	if((isinstance(selection, int)) and (int(selection) > 3 and int(selection) <= 0)): #if it's not one or two
		print("INVALID INPUT")
		return False
	

	if(int(selection) == 1):
		name = input("What is your name? >>> ")
		email = input("What is your email? >>> ")
		password = input("What would you like your password to be? >>> ")
		
		createNewAccount(email, password, name, 0.0)
		print("Clearing in 3 seconds...\n")
		time.sleep(3)
		os.system('cls')
		return True
	elif(int(selection) == 2):
		email = passwordValidation()

		print("Clearing in 3 seconds...\n")
		time.sleep(3)
		os.system('cls')
		
		if(email == "not in system"):
			return menuScreen()
		elif(email == False):
			return False
		else:
			return email
		
	elif(int(selection) == 3):
		#print("Clearing in 3 seconds...\n")
		#time.sleep(3)
		#os.system('cls')
		return False

	
def passwordValidation():
	email = input("What is your email? >>> ")
	password = input("What is your password? >>> ")

	checkPasswordQuery = (f"SELECT Password FROM accounts1 WHERE Email = '{email}';")
	cursor.execute(checkPasswordQuery)

	passwordInSystem = cursor.fetchall()

	if(len(passwordInSystem) == 0):
		print("NOT IN SYSTEM. PLEASE CREATE AN ACCOUNT.")

		return "not in system"

	i = 3
	while(passwordInSystem[0][0] != password and i > 1):
		i -= 1
		print(f"\nWRONG PASSWORD. YOU HAVE {i} TRIES REMAINING.")
		password = input("What is your password? >>> ")
		cursor.execute(checkPasswordQuery)
		passwordInSystem = cursor.fetchall()

	if(i == 1):
		print("BANK ACCOUNT LOCKED. PLEASE RETRY IN A FEW MINUTES.")
		print()
		return False

	getNameQuery = (f"SELECT Name FROM accounts1 WHERE Email = '{email}';")
	cursor.execute(getNameQuery)
	name = cursor.fetchall()

	print(f"\nWelcome {name[0][0]}. ")

	return email


def loginScreen(email):
	print("-----------------------------------------------------------")
	print("---------------------CODE2COLLEGE BANK---------------------")
	print("-----------------------------------------------------------")
	print()


	print("          ACTIONS    ")
	print("---------------------------")
	print("1. View Funds")
	print("2. Deposit Funds")
	print("3. Withdraw Funds")
	print("4. Modify Account Details")
	print("5. Delete Account")
	print("6. Log out")
	print("---------------------------")
	option = input("Select an action >>> ")


	if(option.isalpha()):
		print("INVALID INPUT")
		time.sleep(2)
		os.system('cls')

		return loginScreen(email)

	if(option.isnumeric and (int(option) > 6 or int(option) < 1)):
		print("INVALID INPUT")
		time.sleep(2)
		os.system('cls')

		return loginScreen(email)

	if(int(option) == 1):
		checkAccountBalance(email)
		time.sleep(3)
		os.system('cls')
		return email

	elif(int(option) == 2):
		amountDeposit = input("How many funds? >>> ")
		depositFunds(email, float(amountDeposit))
		time.sleep(3)
		os.system('cls')
		return email

	elif(int(option) == 3):
		amountWithDraw = input("How many funds? >>> ")
		withdrawFunds(email, float(amountWithDraw))
		time.sleep(3)
		os.system('cls')
		return email

	elif(int(option) == 4):
		print("1. Name")
		print("2. Password")
		print("3. Email")

		option = input("What would you like to modify? >>> ")
		value = input("What would you like to change it to? >>> ")


		if(not isinstance(option, int) and int(option) > 4 and int(option) < 0):
			print("INVALID INPUT")
			return

		if(int(option) == 1):
			email = modifyAccountDetails(email, value, "name")
		elif(int(option) == 2):
			email = modifyAccountDetails(email, value, "password")
		elif(int(option) == 3):
			email = modifyAccountDetails(email, value, "email")
		else:
			print("INVALID INPUT")
			return
		
		time.sleep(3)
		os.system('cls')

		return email

	elif(int(option) == 5):
		print("Are you sure you want to delete your account? All your data, including your money, will be wiped from our system.")
		option = input("Indicate yes (y) or no (n) >>> ")
		if(option.lower() == 'yes' or option.lower() == 'y'):
			deleteAccount(email)
		else:
			print("ABORTING DELETE...")
			time.sleep(3)
			os.system('cls')
			return email

		print("\nClearing in 3 seconds...\n")
		time.sleep(3)
		os.system('cls')

		return False
	
	elif (int(option) == 6):
		print("Logging out...")
		time.sleep(3)
		os.system('cls')

		return False


def checkAccountBalance(email):
	print()
	accountBalanceQuery = (f"SELECT Balance FROM accounts1 WHERE Email = '{email}';")
	cursor.execute(accountBalanceQuery)
	#row = cursor.fetchone(accountBalanceQuery)

	#if(row is None):
	#	print("EMAIL NOT FOUND")
	#	return False

	balance = cursor.fetchall()
	print(f"YOUR ACCOUNT DETAILS: {balance[0][0]}")

	return True


def depositFunds(email, amountToDeposit): 
	accountBalanceQuery = (f"SELECT Balance FROM accounts1 WHERE Email = '{email}';")
	cursor.execute(accountBalanceQuery)
	balance = cursor.fetchall()

	#print(f"TROUBLESHOOTING: BALANCE IS {balance[0][0]}.")

	updateFundsQuery = (f"UPDATE accounts1 SET Balance = {float(balance[0][0]) + amountToDeposit} WHERE Email = '{email}';") #get the deposit
	cursor.execute(updateFundsQuery)

	checkAccountBalance(email)

	return True
	

def withdrawFunds(email, amountToWithdraw):
	#first, get the balance in the account
	viewAccountBalanceQuery = (f"SELECT Balance FROM accounts1 WHERE Email = '{email}';")
	cursor.execute(viewAccountBalanceQuery)

	total = cursor.fetchall()

	#update the balance (if it's over the amount to withdraw)
	if(float(total[0][0]) < amountToWithdraw):
		print("NOT ENOUGH FUNDS")
		return False
	else:
		updateFundsQuery = (f"UPDATE accounts1 SET Balance = {float(total[0][0]) - amountToWithdraw} WHERE Email = '{email}';") #get the deposit
		cursor.execute(updateFundsQuery)
		checkAccountBalance(email)


	"""
	getBalanceQuery = (f"SELECT Balance FROM accounts1 WHERE Email = '{email}';") #get the deposit
	cursor.execute(getBalanceQuery)

	if(cursor.fetchone()[0] <= 0):
		print("EMAIL NOT FOUND")
		return False

	newBalance = cursor - amountToWithdraw
	if(newBalance < 0):
		print("NOT SUFFICIENT FUNDS.")
		return False

	addNewBalanceQuery = (f"INSERT INTO accounts1(Email, Balance) VALUES('{email}', {newBalance});")
	cursor.execute(addNewBalanceQuery)
	return True
	"""


def createNewAccount(email, password, name, balance):
	print("THANK YOU. PROCESSING...")

	#print(f"INSERT INTO accounts1 VALUES('{str(name)}', '{str(email)}', '{str(password)}', {float(balance)});")
	#print()
	createAccount = (f"INSERT INTO accounts1 VALUES('{str(name.upper())}', '{str(email.lower())}', '{str(password)}', {float(balance)});")

	cursor.execute(createAccount) #error here

	viewAccountDetails(email)
	print("IF ANYTHING IS INCORRECT, PLEASE DON'T HESITATE TO CHANGE YOUR ACCOUNT DETAILS.")
	return True


def deleteAccount(email):
	#getDeleteQuery = (f"SELECT Email FROM accounts1 WHERE Email = '{email}';") 
	#cursor.execute(getDeleteQuery)
	
	#if(cursor.fetchone()[0] <= 0):
	#	print("EMAIL NOT FOUND")
	#	return False
	
	deleteCommand = (f"DELETE FROM accounts1 WHERE Email = '{email}';")
	cursor.execute(deleteCommand)

	print("...")

	print("ACCOUNT DELETED.")

	return True


def modifyAccountDetails(email, value, columnToChange):
	#three things that can be changed: email, name, and password
 
	if(columnToChange.lower() == 'email'):
		changeRequest = (f"UPDATE accounts1 SET Email = '{value}' WHERE Email = '{email}';")
		email = value

	elif(columnToChange.lower() == 'name'):
		changeRequest = (f"UPDATE accounts1 SET Name = '{value}' WHERE Email = '{email}';")
	elif(columnToChange.lower() == 'password'):
		changeRequest = (f"UPDATE accounts1 SET Password = '{value}' WHERE Email = '{email}';")
	else:
		print("INVALID INPUT.")
		return False
	
	cursor.execute(changeRequest)

	viewAccountDetails(email)

	return email
	
	
def viewAccountDetails(email):
	viewAccountDetailsQuery = (f"SELECT * FROM accounts1 WHERE Email = '{email}'") #get the information from the table
	cursor.execute(viewAccountDetailsQuery)
	accountDetails = cursor.fetchall()

	print("\nYOUR ACCOUNT DETAILS") #print data

	print(f"NAME: {accountDetails[0][0]}")
	print(f"EMAIL: {accountDetails[0][1]}")
	print(f"PASSWORD: {accountDetails[0][2]}")
	print(f"BALANCE: {'{:.2f}'.format(accountDetails[0][3])}")

	print()
	
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
		result = modifyAccountDetails("anushkabhave8@gmail.com", "Anushka Alok Bhave", "name")
		testApplication.assertTrue(result)

	def testDELETEACCOUNT(self):
		result = deleteAccount("anushkabhave8@gmail.com")
		testApplication.assertTrue(result)

print()


result = menuScreen()
while(result == True): # if it returns something to do with creating an account
	result = menuScreen() 
	
	
#while logging in, menuScreen should return email


while(result != False):
	#once user is done with creating account
 
	#if the user returns False, then they've signed out
	#otherwise, the user returns their email (to ensure that, when email is modified, it is correct)
	#in some cases, the function returns itself (recursion). this is used for input validation purposes
	result1 = loginScreen(result)
	while(result1 != False): 
		result1 = loginScreen(result1)
	
	#if menuScreen return False, then the user has terminated the app
	result = menuScreen()
	while(result == True):
		result = menuScreen()


print("Thank you for using Code2College Bank.")
print("SYSTEM TERMINATED.")



cursor.close()
connection.close()