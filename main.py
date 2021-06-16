# this api ilearn place products
import json
from flask import Flask,request,jsonify
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "vicky1598",
    database = "ilearnplace"
    )

mycursor = mydb.cursor()

@app.route('/contactus',methods=['POST'])
def add_contactus():
    record = json.loads(request.data)
    username1 = record["username"]
    usercontact = record["contact"]
    usermessage = record["message"]


    sql = " INSERT INTO contact_us(username,contact,message) VALUES (%s,%s,%s)"
    val = (username1,usercontact,usermessage)

    mycursor.execute(sql,val,)
    mydb.commit()
    response = {"success":True,"message":"added successfully "}
    return jsonify(response)


@app.route('/buynow',methods = ['POST'])
def add_buy_now():
    record = json.loads(request.data)
    contact = record["contact"]
    name = record["product_name"]

    sql = " INSERT INTO Buy_now(contact,product_name) VALUES (%s,%s)"
    val = (contact, name)

    mycursor.execute(sql, val)
    mydb.commit()
    response = {"success":True,"message":"product out of stock, notify you soon "}
    return jsonify(response)

app.run(debug=True)