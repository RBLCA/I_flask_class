from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/' )
def welcome():
    return 'Welcome to the the Flask class.'

@app.route('/calculator', methods = ['GET', 'POST'])
def math_operation():
    operation = request.json["operation"]
    num1 = request.json['num1']
    num2 = request.json['num2']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'multiply':
        result = num1 * num2 

    elif operation == 'division':
        result = num1 / num2
    else:
        result = num1 - num2

    return jsonify(result)






print(__name__)


if __name__ == '__main__':
    app.run(debug=True)