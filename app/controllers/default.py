from app import app


@app.route("/index")
@app.route("/")
def index():
    return "Hello Word!"


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