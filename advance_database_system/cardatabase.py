import sys
import getpass
import MySQLdb
import random 
import datetime

def book_a_car(username):
	
	db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )
	rent_id = random.randint(0,100000)

	cursor = db.cursor()
	results = []


	sql = "SELECT REG_NO,CAR_RATE,BOOK_STATUS,MARK,MODEL,YEAR \
		 FROM CAR,CARTYPE \
		WHERE CAR.MODEL_ID = CARTYPE.MODEL_ID AND CAR.BOOK_STATUS = '%s'"%("not booked")
       		
	try:
   		
   		cursor.execute(sql)
   		
   		results = cursor.fetchall()
		
		num = 0
		print "(MARK,MODEL,YEAR,CAR_RATE,BOOKING STATUS)"
   		for row in results:
      			car_rate = row[1]
      			book_status = row[2]
      			mark = row[3]
      			model = row[4]
			year = row[5]
     
      			print str(num + 1) + ".(%s,%s,%d,%d,%s)" % \
             			(row[3],row[4],row[5],row[1],row[2])
			num = num + 1
		
		
		
		
	except:
   		print "Error: unable to fecth data"

	car_selection= raw_input("Select a number: ")
	
	selected_car = results[int(car_selection)-1]
	
	registration_no = selected_car[0]
	booking_status =  selected_car[2] 

	date = datetime.datetime.now().strftime("%m-%d-%Y")
	next_date =   datetime.datetime.now() + datetime.timedelta(days=1)
	next = str(next_date).split(" ")
	next_date = next[0]

	sql = "UPDATE CAR SET BOOK_STATUS = '%s' WHERE REG_NO = '%s'"%("booked",registration_no)

	try:
	   	
   		cursor.execute(sql)
	   	
   		db.commit()
	except:
   		
   		db.rollback()

	if booking_status == "not booked":
		sql = "INSERT INTO RENT(RENT_ID, \
       			CUST_ID, REG_NO, RENT_DATE, RETURN_DATE) \
       			VALUES ('%s', '%s', '%s', '%s', '%s' )" % \
      		 	(rent_id, username, registration_no, str(date), next_date)
		print "Car booked successfully"
	
		try:
	   		
   			cursor.execute(sql)
	   		
   			db.commit()
		except:
   			
   			db.rollback()
	else:
		print "Car is already booked"

	
	db.close()

	

def return_a_car(username):
	db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )
		
	cursor = db.cursor()
	results = []
	
	sql = "SELECT  RENT_ID,MODEL_ID\
		 FROM RENT,CAR \
		WHERE CUST_ID = '%s' AND RENT.REG_NO = CAR.REG_NO"%(username)

	try:
   			
   		cursor.execute(sql)
   
  		results = cursor.fetchone()
		if len(results): 
			db.commit()
		else:
			print "No cars booked for this user"
      			sys.exit()

			
		
	except:
   		print "No cars booked for this user"
		db.rollback()
		sys.exit()
		
	
	rent_id = results[0]
	model_id = results[1]
	

	sql = "SELECT MARK,MODEL,YEAR FROM CARTYPE \
		WHERE  MODEL_ID = '%s'"%(model_id)
	try:
	   	
   		cursor.execute(sql)
		results = cursor.fetchone()
	   	
		
   		db.commit()
	
		
	except:
   		print "No car found with model id"


	sql = "DELETE FROM RENT WHERE RENT_ID = '%s'"%(rent_id)
	try:
	   	
   		cursor.execute(sql)
	   	
   		db.commit()
	
		
	except:
   		print "Not deleted from RENT table"

	
	sql = "UPDATE CAR SET BOOK_STATUS = '%s' WHERE MODEL_ID = '%s'"%("not booked",model_id)

	

	try:
	   	# Execute the SQL command
   		cursor.execute(sql)
	   	# Commit your changes in the database
   		db.commit()
	except:
   		# Rollback in case there is any error
		print "Updated booking status unsuccessful"
   		db.rollback()

	print "'%s' '%s' '%s' car returned successfully"%(results[0],results[1],results[2])
	
	
	db.close()

def available_cars():
	db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )

	cursor = db.cursor()
	


	sql = "SELECT CAR_RATE,BOOK_STATUS,MARK,MODEL,YEAR \
		 FROM CAR,CARTYPE \
		WHERE CAR.MODEL_ID = CARTYPE.MODEL_ID"
       		
	try:
   		
   		cursor.execute(sql)
   		
   		results = cursor.fetchall()
		
		print "(MARK,MODEL,YEAR,CAR_RATE,BOOKING STATUS)"
   		for row in results:
      			car_rate = row[0]
      			book_status = row[1]
      			mark = row[2]
      			model = row[3]
			year = row[4]
      
      			print ".(%s,%s,%d,%d,%s)" % \
             			(row[2],row[3],row[4],row[0],row[1])
		
	except:
   		print "Error: unable to fecth data"

	

def admin_login():
	pswd = "admin"
	password = getpass.getpass("Enter Admin password: ")	
	while True:
		if(password == pswd):
			break
		else:
			password = getpass.getpass("Enter password again: ")

	
	db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )

	
	cursor = db.cursor()

	model_id = random.randint(0,10000)
	reg_no = random.randint(1000,9999)

	mark = raw_input("Enter manufacturer name:")
	model = raw_input("Enter model: ")
	year = raw_input("Enter year: ")
	car_rate = raw_input("Enter price: ")
	book_status = "not booked"


	sql = "INSERT INTO CARTYPE(MODEL_ID, \
       		MARK,MODEL,YEAR) \
       		VALUES ('%s', '%s', '%s','%d' )" % \
       		(model_id, mark, model, int(year))

	try:
   		
   		cursor.execute(sql)
   		
   		db.commit()
	except:
   		
   		db.rollback()





	sql = "INSERT INTO CAR(REG_NO,MODEL_ID, \
       		CAR_RATE,BOOK_STATUS) \
       		VALUES ('%s', '%s', '%f','%s' )" % \
       		(reg_no, model_id, float(car_rate), book_status)

	try:
   		
   		cursor.execute(sql)
   		
   		db.commit()
	except:
   		
   		db.rollback()



	
	db.close()

	


def car_booking(username):
	print "Please select a transaction from below:"
	print "1.Book a car"
	print "2.Return a car"
	print "3.Check all available cars"
	
	while True:
		num = raw_input("Enter a number: ")
	
		if int(num) == 1:
			book_a_car(username)
			
			break
			
		elif int(num) == 2:
			return_a_car(username)
			break

		elif int(num) == 3:
			available_cars()
			break
		else:
			print "Enter a valid number"
	

	
def login():

	db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	#print "login"

	username = raw_input("Enter username:")
	
	
	
	while True:

		sql = "SELECT CUST_ID,CUST_PASS FROM CUSTOMER \
       			WHERE CUST_ID = '%s'"%(username)
		try:
   			# Execute the SQL command
   			cursor.execute(sql)
   		# Fetch all the rows in a list of lists.
  			results = cursor.fetchone()
      			customer_id = results[0]
			customer_pass = results[1]
			break
		except:
   			print "User name doesn't exist"

	db.close()
	password = getpass.getpass("Enter password:")
	
	while True:
		if(password == customer_pass):
			break
		else:
			password = getpass.getpass("Enter password again: ")
		
		
# disconnect from server
	
	print "Login successfull"
	car_booking(username)
	

def registration():
	
	cust_name = raw_input("Enter your name:")
	cust_id = raw_input("Create a customer id:")
	cust_pswd = getpass.getpass("Create a password:")
	e_mail = raw_input("Enter your mail-id:")
	cust_no = raw_input("Enter your phone number:")

	db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )

# prepare a cursor object using cursor() method
	cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
	sql = "INSERT INTO CUSTOMER(CUST_ID, \
       		CUST_PASS, CUST_NAME, CUST_EMAIL, CUST_NO) \
       		VALUES ('%s', '%s', '%s', '%s', '%s' )" % \
      		 (cust_id, cust_pswd, cust_name, e_mail, cust_no)
	try:
   	# Execute the SQL command
   		cursor.execute(sql)
   	# Commit your changes in the database
   		db.commit()
	except:
   	# Rollback in case there is any error
   		db.rollback()

	# disconnect from server
	db.close()
	
	

	

def main():	
	
	print "***************************************************"
	print "***********Welcome to *****************************"
	print "*********Car booking management system*************"
	print "***************************************************"
	print "Select an option below:"
	print "1.Login if already a user"
	print "2.New user registration"
	print "3.Admin login"


	val = raw_input("Please select a number:")	
	
	if int(val) == 1:
		login()
	elif int(val) == 2:
		registration()
		print "Registration successfull"
	else:
		admin_login()
	


if __name__ == '__main__':
	main()



