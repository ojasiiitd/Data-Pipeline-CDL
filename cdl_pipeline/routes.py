from cdl_pipeline import app
from cdl_pipeline.forms import DataInputForm

from flask import render_template , flash , redirect , url_for , request , jsonify

import pandas as pd

@app.route("/")
# homepage where the root endpoint points to
def homepage():
    return render_template("information.html")

@app.route("/input" , methods = ['GET' , 'POST'])
# user proivides the sequential input using a form here, and also sees the dataset
def inputData():
    form = DataInputForm()

    df_raw = pd.read_csv("data/Assignment Task _ Dataset.csv")


    if request.method == "POST" and form.validate():
        return redirect(url_for("output"))
    return render_template('input.html',
                           df_html = df_raw.sample(7).to_html(classes='table table-striped table-bordered'),
                           form = form)

@app.route("/output")
def output():
    return render_template('report.html')
