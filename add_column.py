import mysqldb
mydb= mysqldb.connector_mysql()

mycursor = mydb.cursor()
def add_emails ():
    result = mycursor.execute("ALTER TABLE contact_us ADD email VARCHAR (255)")
    print(result)
    return result
add_emails()