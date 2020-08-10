#!venv/bin/python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>Hello Flask</h1>
        <p>test heroku</p>
    '''

app.run(host='0.0.0.0')