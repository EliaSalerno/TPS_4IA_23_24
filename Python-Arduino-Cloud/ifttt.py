from flask import Flask,request
import json 

app = Flask(__name__)

@app.route("/",methods = ['POST'])
def stampa():
    d=request.get_json()
    print("stampato: "+d["parm"])
    return("ok")