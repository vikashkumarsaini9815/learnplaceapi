import mysql.connector as my
conn = my.connect(host="localhost",
                  user="root",
                  passwd="",
                  database="ilearnplace")
cur = conn.cursor()
def create():
    c = "create table product" \
        "(product_id int(10) primary key auto_increment," \
        "product_name varchar(50)," \
        "price int(10), " \
        "title varchar(50)," \
        "product_type varchar(50), " \
        "description varchar(255), " \
        "category varchar(50))"
    try:
        cur.execute(c)
        conn.commit()
        print("table created")
    except:
        print("failed")

create()