import mysql.connector
def connector_mysql():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="vicky1598",
        database="ilearnplace"
        )

        return mydb
