import mysqldb
mydb= mysqldb.connector_mysql()

mycursor = mydb.cursor()
def create_table ():
       result =  mycursor.execute("CREATE TABLE contact_us(id INT (5) AUTO_INCREMENT PRIMARY KEY,username VARCHAR (200) ,contact INT (12),message VARCHAR (255))")
       return result
create_table()