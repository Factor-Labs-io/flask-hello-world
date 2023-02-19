from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>The test server for Factor Labs IO</h1>'
