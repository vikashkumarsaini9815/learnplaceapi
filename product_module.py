import mysqldb
mydb= mysqldb.connector_mysql()

mycursor = mydb.cursor()
def create():
    c = "create table productplace" \
        "(product_id int(10) primary key auto_increment," \
        "product_name varchar(50)," \
        "price int(10), " \
        "title varchar(50)," \
        "product_type varchar(50), " \
        "description varchar(255), " \
        "category varchar(50))"
    try:
        mycursor.execute(c)
        mydb.commit()
        print("table created")
    except:
        print("failed")

create()