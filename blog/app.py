from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/home')
def home():
    return '<h1>Welcome to the Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Me:Yu</h1>'
    
if __name__ == '__main__' : 
    app.run()
        