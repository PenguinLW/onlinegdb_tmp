import numpy as np;
from flask import Flask;

app = Flask(__name__);

@app.route('/')
def entrance():
    import temp;
    
    return '<p>be ok.<br><a href=\'https://flask.palletsprojects.com/en/1.1.x/quickstart/\'>hto eto</a></p>';

if(__name__ == '__main__'):
    app.run(port=1111, host='0.0.0.0', debug=True);