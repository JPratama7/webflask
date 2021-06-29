from flask import jsonify
from flask import request
from flask import jsonify
import geoip2
import requests

def ipget():
    return request.remote_addr

def geolocation(ip):
    response = requests.get("https://geolocation-db.com/json/{ip}&position=true".format(ip = ip)).json()
    return response