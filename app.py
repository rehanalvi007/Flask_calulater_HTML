# create simple Flask application
# Import libraries
from flask import Flask,request,render_template

#Instantiate the Flask module
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def calculater():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']
        result = perform_operation(num1,num2,operation)
        return render_template('result.html', num1=num1, num2=num2, operation=operation, result=result)
    return render_template('index.html')


def perform_operation(num1,num2,operation):
    if operation =='addition':
        return num1 + num2
    if operation == 'subtract':
        return num1 - num2
    if operation == 'multiply':
        return num1 * num2
    if operation == 'divide':
        return num1 / num2


if __name__ == '__main__':
    app.run(debug=True)