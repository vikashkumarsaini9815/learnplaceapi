from flask import Flask, request, json, jsonify
import mysql.connector as my

app = Flask(__name__)

conn = my.connect(host="localhost",
                  user="root",
                  passwd="",
                  database="ilearnplace")
cur = conn.cursor()
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
            cur.execute(s)
            conn.commit()
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
        cur.execute(s)
        conn.commit()
        response={"sucess":True}
        return jsonify(response)

@app.route('/product', methods=['GET'])
def retrive():
    if request.method == "GET":
        s = "select * from product"
        cur.execute(s)
        data = cur.fetchall()
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
        cur.execute(s)
        conn.commit()
        response={"sucess":True}
        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)     # run the flask app