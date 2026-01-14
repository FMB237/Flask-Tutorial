#This is the python file where i gonna used to build forms and handle files using the flask micro-framework
#So let jst build a simple page
import pandas as pd
from flask import Flask,make_response,request,render_template,url_for
#These are all the modules we have learn from now

app=Flask(__name__,template_folder="templates")

#Let add a simple route
@app.route('/')
def index():
    return f'Hello Bro'
#We gonna create a route for other forms.html file
@app.route('/form',methods=["GET","POST"]) 
def form():
    if request.method =="GET":
        return render_template('form.html')   
    elif (request.method=="POST"):
        username = request.form.get('username') #This is the name of the input we want to get
        password =request.form.get('password') #Always make sure the names are correct to that of the html form
        email= request.form.get('email')
        #Let add some Sucees Login conditions
        if username== "Miguel" and password =='Th@9Sand'and email=="miguelfouenanf@gmail.com":
            return "<h1>Sucessful Login</h1>"
        else:
            return 'Login Failed'

#Let Create and endpoint to hanble files upload
@app.route("/upload", methods=["POST"])
def upload():
    file= request.files["file"] #Which is the name of the file in the form.html
    if file.content_type=="text/plain":
        return file.read().decode()
    elif (file.content_type ==  "application/vnd.ms-excel" or file.content_type=="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"):
            df=pd.read.excel(file)
            return df.to_html()

app.run(debug=True,host="0.0.0.0",port=5000)
