'''app.py'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    '''
    This is a docstring
    '''
    return "<p>hello continuos world</p>"

if __name__ == "__main__":
    app.run()
