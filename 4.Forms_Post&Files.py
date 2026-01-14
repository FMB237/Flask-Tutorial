#This is the python file where i gonna used to build forms and handle files using the flask micro-framework
#So let jst build a simple page

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


app.run(debug=True,host="0.0.0.0",port=5000)
