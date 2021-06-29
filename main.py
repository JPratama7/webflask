from flask import Flask
from module import ipget, geolocation
from flask import render_template


app = Flask(__name__)



@app.route("/")
@app.route("/index")
def homepage():
    ip = ipget()
    location = geolocation(ip)
    negara = location['country_name']
    kota = location['city']
    return "WELKOM TO MAI WEBSITE"
    #return render_template('index.html', ip = ip, negara = negara, kota = kota)
    
