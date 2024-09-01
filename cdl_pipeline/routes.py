from cdl_pipeline import app
from cdl_pipeline import models

from flask import render_template

@app.route("/")
def home():
    return "<h1>CivicDataLab</h1>"

@app.route("/input")
def s():
    return "<h1>CivicDataLab - Input</h1>"