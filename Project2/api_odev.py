from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd
import requests

app = Flask(__name__)

api = Api(app)

class Earthquake(Resource):

   def get(self,minmagnitude):

       url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-01-01&endtime=2023-12-31&minlatitude=26&maxlatitude=45&minlongitude=36&maxlongitude=42&minmagnitude="+ minmagnitude


       response = requests.get(url)

       data = response.json()

       return {'features' : data['features']}, 200

api.add_resource(Earthquake, '/earthquake/<string:minmagnitude>')

if __name__ == '__main__':

   app.run(host="0.0.0.0", port=6767)

   app.run()
