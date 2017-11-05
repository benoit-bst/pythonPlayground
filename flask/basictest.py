#!/usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def accueil():
  mots = ["bonjour", "a", "toi", "visiteur."]
  return render_template('accueil.html', titre="bienvenu !", mots=mots)

@app.route("/page2-test/")
@app.route("/page2/")
def page2():
  return "Page 2 : " + request.path

@app.route("/contact/")
def contact():
  mail = "bbst@tdev"
  tel = "+336 22 79 02 19"
  return "Mail : {} - tel : {}".format(mail, tel)

if __name__ == "__main__":
  app.run(debug=True)