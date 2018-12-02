from flask import Flask, render_template, request
import math
import csv
from trainmodel import m

app = Flask(__name__)

country = "countries.csv"

countries = []

with open(country, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        for col in row:
            countries.append(col.strip())

model = m()


@app.route("/")
def index():
    return render_template("index.html", countries=countries)


@app.route("/prediction", methods=["POST"])
def predict():
    c = request.form.get("countries")
    y = request.form.get("year")
    y = int(y)
    c = int(c) - 1
    ans = math.floor(model[c][0] + (y - 1960) * model[c][1])
    # return render_template("success.html", population=ans)
    return render_template("index.html", countries=countries, population=ans)
