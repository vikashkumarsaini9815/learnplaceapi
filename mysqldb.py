import mysql.connector
def connector_mysql():
        mydb = mysql.connector.connect(
        host="localhost",
        user="ilearnplace",
        password="ilearnplace",
        database="ilearnplace"
        )

        return mydb
