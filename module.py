from flask import jsonify
from flask import request
from flask import jsonify
import requests


def ipget():
    return request.remote_addr

def geolocation(ip):
    response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true".json())
    print(response)
    return response

