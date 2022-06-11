'''app.py'''

from flask import Flask, render_template, request

def suma(a=0,b=0):
    return (a + b)

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
