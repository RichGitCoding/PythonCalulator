import sys
import requests
from os import rename
import statistics
from flask import Flask, render_template, request, url_for, redirect
from wtforms import Form, FloatField, validators
import math


#len() get length of sample
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')

@app.route('/send', methods=["POST"])
def send():
    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operation = request.form["operation"]
        if operation == "add":
            sum = float(num1)+ float(num2)
            return render_template('app.html',sum=sum)
        elif operation == "subtract":
            sum = float(num1)-float(num2)
            return render_template('app.html',sum=sum)
        elif operation == "multiply":
            sum = float(num1)*float(num2)
            return render_template('app.html',sum=sum)
        elif operation == "divide":
            sum = float(num2)/float(num1)
            return render_template('app.html',sum=sum)
        else:
            return render_template('app.html')
        
    

  
if __name__ == '__main__':
   app.run(debug = True)













