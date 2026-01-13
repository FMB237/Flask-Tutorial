#This will mainly be simple flask app

from  flask import Flask

app= Flask(__name__)

@app.route('/')
def index():
    return'Hello World'
#Let add another page
@app.route('/home')
def home():
    return '<h1>This is the home page </h1>'
if __name__== '__main__':
    app.run(host="0.0.0.0", port= 4000,debug=True)  #By putting port=3000 our app will now run on port 3000   