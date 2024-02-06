from flask import Flask,request

app = Flask(__name__)
#--------------------------------------------------------------------------
# invia il form vuoto
#--------------------------------------------------------------------------
@app.route("/")
def inviaFormVuoto():
    f='''
    <html>
        <head>
            <title>Esempio Form</title>
        </head>
        <body>
            <form action="/ricevi">
                <label>Materia:</label>
                <input type="text" name="materia"><br><br>
                <input type="submit" value="Invia">
            </form> 
        </body>
    </html> 
    '''
    return(f)
#--------------------------------------------------------------------------
# riceve i dati del form e li visualizza
#--------------------------------------------------------------------------
@app.route("/ricevi")
def riceviForm():
    return(request.args["materia"])