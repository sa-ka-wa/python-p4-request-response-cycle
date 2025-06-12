#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

@app.route('/print/parameter')
def print_string(parameter):
    print (parameter)
    return (parameter)

@app.route('/count/<int:parameter>')
def count(parameter):
    number = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers

@app.route('/math/<int:num1>/<operation>/<Iint:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
