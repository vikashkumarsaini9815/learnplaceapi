import mysqldb
mydb= mysqldb.connector_mysql()

mycursor = mydb.cursor()
def create_table ():
       result =  mycursor.execute("CREATE TABLE Buy_now(id INT (5) AUTO_INCREMENT PRIMARY KEY,contact INT (255)NOT Null,product_name varchar (250))")
       return result
create_table()