## Integrate HTML with Flask
## HTTP verb GET and POST
## Jinja2 template engine

'''
{%.....%} statements
{{   }} expressions to print variables
{#......#} this is for comments

'''

from cgitb import reset
import re
from unittest import result
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') 

@app.route('/success/<int:score>')
def success(score):
    return render_template('result.html',result='PASSED') 

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('result.html',result='FAILED') 


## This will be result checker
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0

    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['C'])
        datascience= float(request.form['datascience'])

        total_score = (science+maths+c+datascience)/4

        return render_template('result.html',result=total_score)
    

if __name__=="__main__":
    app.run(debug=True)
