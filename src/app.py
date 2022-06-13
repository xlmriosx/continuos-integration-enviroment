'''app.py'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    '''
    This is a docstring
    '''
    return "hello continuos world 2"

if __name__ == "__main__":
    app.run()
