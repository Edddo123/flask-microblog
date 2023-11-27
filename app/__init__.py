from flask import Flask

# This is app variable instance of flask
app = Flask(__name__)

# This app is module, we named directoy app and created init.py. So we created app directory.
from app import routes