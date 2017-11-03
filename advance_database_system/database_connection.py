
import MySQLdb
import random

# Open database connection
db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

model_id = random.randint(0,10000)
reg_no = random.randint(1000,9999)

mark = raw_input("Enter manufacturer name:")
model = raw_input("Enter model: ")
year = raw_input("Enter year: ")
car_rate = raw_input("Enter price: ")
book_status = "not booked"



'''
sql = "SELECT * FROM CARTYPE"

while True:
	try:
		model_id = random.randint(0,10000)
   		# Execute the SQL command
		print "execute"
   		cursor.execute(sql)
		print "after execute"
   		# Fetch all the rows in a list of lists.
  		results = cursor.fetchall()
		

   		for row in results:
			if row[0] == model_id:
				continue
			else: 
				break
	except:
   		print "Unable to fetch data"'''

# Drop table if it already exist using execute() method.
sql = "INSERT INTO CARTYPE(MODEL_ID, \
       MARK,MODEL,YEAR) \
       VALUES ('%s', '%s', '%s','%d' )" % \
       (model_id, mark, model, int(year))

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()



# disconnect from server


sql = "INSERT INTO CAR(REG_NO,MODEL_ID, \
       CAR_RATE,BOOK_STATUS) \
       VALUES ('%s', '%s', '%f','%s' )" % \
       (reg_no, model_id, float(car_rate), book_status)

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





'''CREATE TABLE CUSTOMER (
         CUST_ID  VARCHAR(20) NOT NULL,
	 CUST_PASS VARCHAR(10),
         CUST_NAME  VARCHAR(20),
         CUST_EMAIL VARCHAR(20),  
         CUST_NO VARCHAR(10),
         )'''
