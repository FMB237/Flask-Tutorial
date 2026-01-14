# This is a full flask course i'm actually starting in 2026 
This course will mainly be build from a Youtube video from the Youtubers now as neuroline 
This course covers almost all what we have to know about flask and how it is use to build web applications

# What is Flask
What is a light-weight python framwork used in building fast and ready production web applications
So flask permit to build fast ready productions app using python

# FLASK !== Django !== FASTAPI
Django and FastAPI are differcent from flask which is more faster and lighter in usage 
Generally flask is used for building fast small app 
Flask has fast and small libraries that permits to build full-stack app very fast
# Render Engine
Flask has a render engine which permit it to run simple html files So the frontend part of the app does not relies on any framework if wanted by the user

# Now let Create our virtual environment on linux mint

python3 -m venv venv
Then start the environment

source vevn/bin/activate
Note :Flask app are run defautly on port 5000
But this can be change the and also the can be run directly on a server and only adding or putting the server ip

# Lesson 1 Basic Flask app
The file for it is know as app.py  where you will find all the basics command and code to run
a simple flask app on your machine

# Lesson 2 Routes & Urls
In this lesson file we gonna file find how to add new routes to our app 
2.Now to handle URLs and types of Urls which are mainly GET and POST Requests
3.Routes are mainly consider as end-points.
4.When handling require we can see if everything is functional using curl on linux and Mac
5.When Using curl we can use either a get or post request for url management

that is 
# These are some examples

curl http://127.0.0.1:5000/contact
curl -X  PORT http://127.0.0.1:contact
curl -X  GET curl http://127.0.0.1:5000/contact
# Depending on the method we have to used we can have the following formats
@app.route('/contact' ,methods=["GET","POST","PUT"])  Some thing like 

When talking about web codes and errors we mainly have many situations on that 
Status 200 : Everything Works find
Status 300 : Where it start for redirections
Status 400
Status 404 : Nothing Found

# Lesson 3 Templates & HTML
As  i said easier flasks has a template render engine which permit it to directly return html pages 
Even if this pages are been style and With Js event and effect flask manages this without the help of any external library
Flask also permit to make prebuild templates of our app that can be used later
All this rendering process is mainly made by the jinja2 rendering engine
For template rendering we need  a directory that will have hold our templates to render So let create that 
Inside that we can create a simple index.html file to render and also let move on to it
# In Flask we can build a General Template model that will hag the general style of our  page model
This file is somethin name in project has the base.html and using jinja2 it is the parent file that styles the other files in our project
In our python code import the module render_templates
In the definition of our application we will the general folder app directory
Using the Jinja2 Engine and python we can dynamically render that is a value can be insert to the backendd from the frontend using this process 
We just create  a variable in the backend and using a paragraph and heading with double calibrasing to represent that 
We can do more advance stuff using jinja2 like rendering a list of items from the backend to the frontend
If we can used a for loop then we can used condtions using the if statement
As i said the process and taking properties from file to one another is known as inheritance
This templates inheritance uses mainly blocks and names to process the data
Now let handle the notion of filters which will mainly permit to handle other operations
Jinja2 has some build features that permits to facilitate some features like the uppercase and lowercase 
Still when using Jinja2 we can build our now features in python
Like a built a reverse string funtions to be used in the other.html file
Now let move on to the used of dynamic URL in flask which can directly be insert inside our code
Then Create a URL from index.html to other.html
But before all that we need to import a module url_for in our python code
So this method of using URL can permit constantly change url directions 

# Lesson4:FORMS,POST,Files
Here this how to handle Forms and files using POST requests.
So let create a file for this form handling and other operations
Create a Form Tag into the Html code and used the method POST
Now just create Good form that we will use to handle this request using the request module from flask
Then just used the post application to treat the data from the form passing through their inputs
e.g # username = requets.form.get('useranme') to get username from out form
The used of form is mainly to get the items from the form in particular
From the form.html  associated with 4.Forms_Post&Files.py we can now mainly manage a simple form
Now let create a File upload and to better handle data
In the same file let create a new form for our file_upload
Now let render our upload data inside a Table
to do this we gonna install and import the python module pandas
e.g import pandas as pd
