from ast import Return
from asyncio.windows_events import NULL
from flaskr import app
from flask import render_template,request
from flaskr.courses import Search,Edx,Links
from flaskr.news import news_buddy
from flaskr.math import Differentiation,Integration,deq
from flaskr.projects import getdata,sorting,project_txt

@app.route("/")
def home_page():
    return render_template('homepage.html')

entry = ''

@app.route("/courses",methods =["GET", "POST"])
def course_page(): 
    if request.method == "POST":
        global entry
        if request.form.get('course'):
            entry = request.form.get('course')
        one = request.form.get("1")
        two = request.form.get("2")
        three = request.form.get("3")
        four = request.form.get("4")
        if entry == '':
            item = []
        elif one is not None:
            item = Links(entry,1)
        elif two is not None:
            item = Links(entry,2)
        elif three is not None:
            item = Links(entry,3)
        elif four is not None:
            item = Links(entry,4)
        else:
            item = Links(entry,1)
        return render_template("courses.html",items = item)
    
    return render_template("courses.html",items = [])

@app.route("/math",methods = ["GET","POST"])
def math_page() :
    if request.method == "POST":
        entry1 = request.form.get('eq1')
        entry2 = request.form.get('eq2')
        entry3 = request.form.get('eq3')
        eq1 = ' '
        eq2 = ' '
        if entry1 is not None :
            eq1 = Differentiation(entry1)
        elif entry2 is not None:
            eq2 = Integration(entry2)
        elif entry3 is not None:
            deq(entry3) 
        
        return render_template('math.html',eq1 = eq1,eq2=eq2)
    return render_template("math.html",eq1 = ' ',eq2= ' ')


@app.route("/news",methods = ["GET","POST"])
def news_page() :
    if request.method == "POST":
        one = request.form.get("1")
        two = request.form.get("2")
        three = request.form.get("3")
        four = request.form.get("4")
        five = request.form.get("5")
        if one is not None:
            item = news_buddy('Education')
        elif two is not None:
            item = news_buddy('Sports')
        elif three is not None:
            item = news_buddy('Science')
        elif four is not None:
            item = news_buddy('Technology')
        elif five is not None:
            item = news_buddy('Medicine')
        
        return render_template("news.html",items = item)
    return render_template("news.html",items = [])

@app.route("/project",methods = ["GET","POST"])
def project_page() :
    if request.method == 'POST':
        entry = request.form.get('query')
        paras = project_txt(entry)
        return render_template("project.html",paras = paras)
    return render_template("project.html",paras = [])

