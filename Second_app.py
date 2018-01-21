from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def welcome():
	return "welcome"
	
@app.route("/hello",methods=["GET","POST"])
def hello():
	request_data=request.args
	if request_data['username']=="admin" and request_data['pwd']=="pass":
		return "success"
	else:
		return"failure"
		
if __name__=="__main__":
	app.run(host="127.0.0.1",port=8001,debug="true")
