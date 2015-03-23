#!venv/bin/python 
from flask_demo import app

if __name__ == '__main__':
  app.debug = True
  app.run('0.0.0.0', 5000)
