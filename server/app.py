#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:number>')
def count(number):
    for i in range(number):
        yield f'{i}\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    if operation == 'div':
        result = eval(f'{num1}/{num2}')
        return f'{result}'
    result = eval(f'{num1}{operation}{num2}')
    return f'{result}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
