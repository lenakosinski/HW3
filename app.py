from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display = "", pageTitle = 'My Calculator')

@app.route('/lena')
def lena():
    return "heyyyy"

if __name__ == '__main__':
    app.run(debug=True)