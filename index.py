from flask import Flask
from flask import request, render_template, redirect,  url_for

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/difficulty')
def index():
    return render_template('level.html')

if __name__ == "__main__":
    app.run()