from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """Subtract and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)

@app.route("/mult")
def do_mult():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)

@app.route("/div")
def do_div():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

### PART TWO

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)

'''# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def do_add():
    'add a and b parameters'
    a = int(request.arg.get('a'))
    b = int(request.arg.get('b'))
    results = a+b
    return str(results)

@app.route('/sub')
def do_sub():
    'subtracting a and b parameters'
    a = int(request.arg.get('a'))
    b = int(request.arg.get('b'))
    results = a-b
    return str(results)

@app.route('/mult')
def do_mult():
    'multiplying a and b parameters'
    a = int(request.arg.get('a'))
    b = int(request.arg.get('b'))
    results = a*b
    return str(results)

@app.route('/div')    
def do_div():
    'dividing a and b parameters'
    a = int(request.arg.get('a'))
    b = int(request.arg.get('b'))
    results = a/b
    return str(results)

'''Part Two'''

funcs ={
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}
@app.route('/funcs')
def funcs (oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)'''