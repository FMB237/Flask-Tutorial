#So now Let do a simple flak app

from flask import Flask,request,make_response,render_template,url_for

app=Flask(__name__,template_folder="templates")

@app.route("/")
def index():
    Myage=21
    Role="Network engineering Student"
    Myskills=["html","CSS","Javascript","linux","Cisco_packer Tracer","GNS3","Bilingual","Python"]
    return render_template('index.html' ,Myage=Myage, Role=Role,Myskills=Myskills)  #let return this varaibles into the index.html file

@app.route("/other")
def other():
    some_text="Filters"
    return render_template('other.html',some_text=some_text)

@app.template_filter("reverse_string")
def reverse_strings(s):
    return s[::-1]

#Let add another personal build functions
@app.template_filter('repeat')
def repeat(s,times=2):
    return  s* times


app.run(debug=True,host="0.0.0.0",port=5555)
