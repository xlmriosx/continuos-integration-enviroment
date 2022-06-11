'''app.py'''

from flask import Flask, render_template, request

def suma(number1=0,number2=0):
    '''
    docstring
    '''
    return number1 + number2

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    '''
    This is a docstring
    '''
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        sum12 = suma(int(num1), int(num2))
        return render_template('suma.html', suma=sum12)

    return render_template('index.html')

if __name__ == "__main__":
    app.run()
