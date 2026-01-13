#This is a recall file to used flask

from flask import Flask,request,make_response    #Also import our request module to our flask code 
#Let also import the response module to flask for fast and direct response


app=Flask(__name__)

@app.route("/")
def home():
    return'Recalling using Flask'

#Let text some response in flask
@app.route("/hello")
def Hello():
    response =make_response("Hello World")
    response.status_code= 202
    response.headers['content-type'] = "application/octet-stream-"
    return  response #So this is like that a response in been made in flask 
#Now let add some other routes

@app.route('/contact')
def contact():
    return '<h1>This is the contact page</h1>'

#In the last lesson i mainly saw how to return dynamic routes

@app.route("/users/<username>")
def users(username):
    return f'<h1> Hello  {username} </h1>'

@app.route("/users/<int:id>") #Here we mainly deside that id is an integer so i no intergers are been type the we gonna have an error
def MyId(id):
    return f" <h1> Use id is :{id} </h1>"
#After that when seen to Adding data in the background using backend

@app.route('/users/<int:number1>/<int:number2>')
def adding(number1,number2): #Le tapss 2 paramaters in this funtion
     return f' The somme of number  {number1} +{number2} = {number1 +number2} '

#Now let recall how to handle Urls
@app.route("/handle",methods=["POST"])
def handle():
    if request.method =='POST':
        greeting =request.args.get('greeting',"Hello")
        name= request.args.get('name','Bruce')
        return f'{greeting} {name}'
    else:
            return f"ERROR POST REQUEST NOT ALLOWED"

#We can also get a full response By importing the flask module response            
   
app.run(host="0.0.0.0",debug=True,port=3000)