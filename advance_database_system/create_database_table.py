
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","toor","CARRENTALDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS CUSTOMER")

# Create table as per requirement
sql = """CREATE TABLE RENT(
	 RENT_ID varchar(20)NOT NULL,
         CUST_ID  varchar(20),
	 REG_NO varchar(20),
	 RENT_DATE varchar(20),
	 RETURN_DATE varchar(20),
	 PRIMARY KEY (RENT_ID)
         )"""


cursor.execute(sql)

# disconnect from server
db.close()
