from flask import Flask, render_template, request
from math import factorial

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('factorial.html')

@app.route('/factorial', methods=['POST'])
def factorial_result():
    number = int(request.form['number'])
    result = factorial(number)
    return render_template('factorial.html', result=result, number=number)

if __name__ == '__main__':
    app.run(debug=True)
