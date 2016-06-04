import flask
from flask import Flask, render_template
import json
import requests
import xmpp

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "asdasd"

if __name__ == '__main__':
    app.debug = True
    app.run()
