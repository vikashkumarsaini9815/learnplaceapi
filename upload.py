from flask import Flask, request, jsonify
import os
import mysql.connector as my

app = Flask(__name__)
app.config["IMAGE_UPLOADS"]="D:/pooja/pythonprogram/ilearnplace/files/"

conn = my.connect(host="localhost",
                  user="root",
                  passwd="",
                  database="ilearnplace")
cur = conn.cursor()

@app.route("/upload", methods=["POST"])
def upload():
	if request.method == "POST":
		f = request.files['file']
		f.save(os.path.join(app.config["IMAGE_UPLOADS"],f.filename))
		path = app.config["IMAGE_UPLOADS"]+f.filename
		s = "insert into product(file) values ('{}')".format(path)
		cur.execute(s)
		conn.commit()
		response = {"sucess": True}
		return jsonify(response)

if __name__=='__main__':
    app.run (debug=True)
