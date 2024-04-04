#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:integer>')
def count(integer):
    result = ''
    for i in range(integer):
        result += f'{i}\n'
    return result    

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'div':
        return str(num1 / num2)
    elif operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '%':
        return str(num1 % num2)
    elif operation == '*':
        return str(num1 * num2)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
