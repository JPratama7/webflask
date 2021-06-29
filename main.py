from flask import Flask
from module import ipget, geolocation
from flask import render_template


app = Flask(__name__)



@app.route("/", methods=["GET"])
def homepage():
    ip = ipget()
    location = geolocation(ip)
    negara = location['country_name']
    kota = location['city']
    return render_template('index.html', ip = ip, negara = negara, kota = kota)
    
if __name__ == '__main__':
    app.run(debug=True)