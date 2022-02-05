## Building the URL Dynamically
#### Variable Rules and Rules Building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to My youtube channel" 

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and the marks is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is "+str(score)

## Result Checker
@app.route('/results/<int:score>')
def results(score):
    if score<50:
        result = 'fail'

    else:
        result = 'success'
    
    return redirect(url_for(result,score=score))

if __name__=="__main__":
    app.run(debug=True)