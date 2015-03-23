from flask import Flask, url_for
import os

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'SECRET_KEY'

from flask_demo import routes
