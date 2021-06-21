# this api ilearn place products
import json
from flask import Flask,request,jsonify
import mysqldb

app = Flask(__name__)

mydb= mysqldb.connector_mysql()

mycursor = mydb.cursor()



@app.route('/contactus',methods=['POST'])
def add_contactus():
    record = json.loads(request.data)
    username1 = record["username"]
    usercontact = record["contact"]
    useremail = record["email"]
    usermessage = record["message"]


    sql = " INSERT INTO contact_us(username,contact,email,message) VALUES (%s,%s,%s,%s)"
    val = (username1,usercontact,useremail,usermessage)

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
# pooja


@app.route('/product', methods=['POST'])
def insert():
        if request.method == "POST":
            _json = request.json
            product_name = _json['product_name']
            price = _json['price']
            title = _json['title']
            product_type = _json['product_type']
            description = _json['description']
            category = _json['category']
            s = "insert into product(product_name, price, title, product_type, description, category) " \
                "values ('{}','{}','{}','{}','{}','{}')".format(product_name, price, title, product_type, description, category)
            mycursor.execute(s)
            mydb.commit()
            response={"sucess":True}
            return jsonify(response)

@app.route('/product', methods=['PUT'])
def update():
    if request.method == "PUT":
        _json = request.json
        product_name = _json['product_name']
        price = _json['price']
        title = _json['title']
        product_type = _json['product_type']
        description = _json['description']
        category = _json['category']
        s = "update product set price = '{}', title ='{}', product_type = '{}', description = '{}', category = '{}' where product_name = '{}'"\
            .format(price, title, product_type, description, category, product_name)
        mycursor.execute(s)
        mydb.commit()
        response={"sucess":True}
        return jsonify(response)

@app.route('/product', methods=['GET'])
def retrive():
    if request.method == "GET":
        s = "select * from product"
        mycursor.execute(s)
        data = mycursor.fetchall()
        payload=[]
        for i in data:
            content = {'product_id':i[0],
                       'product_name':i[1],
                       'price':i[2],
                        'title':i[3],
                        'product_type':i[4],
                        'description':i[5],
                        'category':i[6]
                       }
            payload.append(content)
        return jsonify(payload)

@app.route('/product', methods=['DELETE'])
def delete():
    if request.method == "DELETE":
        _json = request.json
        product_name = _json['product_name']
        s = "delete from product where product_name = '{}'".format(product_name)
        mycursor.execute(s)
        mydb.commit()
        response={"sucess":True}
        return jsonify(response)

app.run(host="0.0.0.0", port=5000,debug=True)
