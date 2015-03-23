from flask import render_template
from flask_demo import app 

@app.route('/')
def index():
  message = "Hello World"
  return render_template('index.html', message=message)
