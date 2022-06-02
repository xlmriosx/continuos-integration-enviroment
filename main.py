'''main.py'''

from flask import Flask

app = Flask(__name__)

@app.route( "/" )
def index(): 
    '''
    This is a docstring
    '''
    return "hello continuos world"

if __name__ == "__main__":
    app.run()
