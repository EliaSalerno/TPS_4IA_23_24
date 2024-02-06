from flask import Flask,request,render_template


app = Flask(__name__)

#--------------------------------------------------------------------------
# invia il form vuoto
#--------------------------------------------------------------------------
@app.route("/")
def inviaFormVuoto():
    return(render_template("form1.html"))

#--------------------------------------------------------------------------
# riceve i dati del form e li visualizza
#--------------------------------------------------------------------------
@app.route("/ricevi")
def riceviForm():
    return(request.args["materia"])