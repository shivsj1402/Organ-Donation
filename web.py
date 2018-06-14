from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'hello group16 -hemant shiv pratik'
  return 'this is my dev branch-pratik'
