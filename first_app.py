from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def welocme():
	return "welcome to first page"
#Variable
@app.route("/hello/<name>")
def helloname(name):
	return "hello %s "% name
@app.route("/hello/<int:roll>")
def roll_no(roll):
	return "roll_no %d "% roll
@app.route("/hello/<float:per>")
def per(per):
	return "you got per %f"% per
	
	
@app.route("/user/<name>")
def user(name):
	if name =="admin":
		return redirect(url_for("hello_admin"))
	else:
		 return redirect(url_for('hello_guest',guest= name))
@app.route("/hello_admin")
def hello_admin():
	return "welcome to Admin page"

@app.route("/hello_guest/<guest>")
def hello_guest(guest):
	return "welcome to guest page"

if __name__=="__main__":
	app.run(host="127.0.0.1",debug="true",port=8092)
