from flask import Flask,request

app = Flask(__name__)

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
                <input type="radio" id="html" name="fav_language" value="HTML">
<label for="html">HTML</label><br>
<input type="radio" id="css" name="fav_language" value="CSS">
<label for="css">CSS</label><br>
<input type="radio" id="javascript" name="fav_language" value="JavaScript">
<label for="javascript">JavaScript</label>
                <input type="submit" value="Invia">
            </form> 
        </body>
    </html> 
    '''
    return(f)

@app.route("/ricevi")
def riceviForm():
    print(request.args)
    return(request.args["materia"])