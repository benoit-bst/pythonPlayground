#!/usr/bin/python
# -*- coding:utf-8 -*-

#
# ./testRestFull.py
# and 
# curl -i http://127.0.0.1:5000/
#

from flask import Flask, render_template
from flask_restful import Api, Resource
from flask_restful.representations import json

app = Flask(__name__)

rest_api = Api(app, catch_all_404s=True, serve_challenge_on_401=True)

class Todo(Resource):
    def get(self, lon=None, lat=None):
        return 1

@app.route("/")
def accueil():
  mots = ["bonjour", "a", "toi", "visiteur."]
  return render_template('accueil.html', titre="bienvenu !", mots=mots)

lon_lat = '<float:lon>;<float:lat>/'
rest_api.add_resource(  Todo,
                        '/coord/' + lon_lat,
                        '/coords/' + lon_lat,
                        endpoint='places')

if __name__ == "__main__":
  app.run(debug=True)
