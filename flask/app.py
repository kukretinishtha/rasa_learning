from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'This is rasa bot apis'

@app.route("/chat")
def index():  
    return render_template('app.html')

if __name__ == '__main__':
    app.run()