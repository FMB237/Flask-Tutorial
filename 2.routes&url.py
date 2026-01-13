#In this file let how URLs and Routes functions in flask

from flask import Flask,request

app= Flask(__name__)

@app.route('/')
def index():
    return '<h1>Bruce Server</h1>'

#Let add a new routes
@app.route('/contact' ,methods=["GET","POST","PUT"]) #Now let check the method used into our code
def contact():
    if request.method == 'GET':
        return 'You have made a GET Request'
    elif (request.method == "POST"):
         return 'You have made a POST Request'
    else:
        return "<h1>This is the return page</h1>"
           

    


@app.route('/about')
def about():
    return '<p> Hey I am Miguel Bruce a 💻 Full-Stack Developer | 🐧 Linux Enthusiast | 🌐 Network & Automation Lover</p>'

#Now let create a dynamic route and pass to it some informations

@app.route('/greet/<name>')
def greet(name):
    return f'Hello {name}'     #This dynamic routes can also be used in id selections
@app.route("/user/<int:id>")
def user(id): 
    return f'The user id :{id}' #We can directly specified the type
#Let somme 2 numbers using this methods and renders

@app.route('/add/<int:number1>/<int:number2>')
def add(number1,number2): #Funtions have 2 paramters
    return f'{number1} + {number2} = {number1 + number2}'    

#Now let learn how to handle requests
@app.route('/handle_url_params') #return str(request.args)
def handle():
    greeting =request.args.get('greeting',"Hello")  #Now let handle that mainly
    name = request.args.get('name','Miguel')
    return f'{greeting}, {name}'   

    


    #With this we gonna display a list and characters

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)