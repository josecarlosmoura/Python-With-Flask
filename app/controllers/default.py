from flask import render_template
from app import app


@app.route("/index/<user>")
@app.route("/", defaults = {"user" : None})
def index(user):
    #Function to retur and render tamplate or simple page HTML
    #Send the parameter user to template to do binding
    return render_template('index.html', user = user)

#Sample with how return a single page HTML
# @app.route("/index")
# @app.route("/")
# def index():
#     return """
#     <html>
#         <head>
#             <title>Hello World!</title>
#         </head>
#         <body>
#             <h1>Hello world!</h1>
#         </body>
#     </html>
#     """


#End point send a string with parameter
@app.route("/user", defaults = {'name' : None})
@app.route("/user/<name>")
def test(name):
    if name:
        return "Olá, %s!" % name
    else:
        return "Olá usuário!"


#End point send a int number with parameter
@app.route("/number_int/<int:number>")
def number_int(number):
        return "Você digitou %i." % number