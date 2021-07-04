from flask import Flask
from module import ipget, geolocation
from flask import render_template


app = Flask(__name__)



@app.route("/heh")
@app.route("/index")
def homepage():
    return render_template('index.html')

@app.route("/")
def test():
    return render_template('tUGAS.html',)

if __name__ == '__main__':
    app.run(debug=True)