from cdl_pipeline import app
from cdl_pipeline.forms import DataInputForm

from flask import render_template , flash , redirect , url_for , request , jsonify , session

import pandas as pd

@app.route("/")
# homepage where the root endpoint points to
def homepage():
    return render_template("information.html")

@app.route("/input" , methods = ['GET' , 'POST'])
# user proivides the sequential input using a form here, and also sees the dataset
def inputData():
    form = DataInputForm(request.form)

    df_raw = pd.read_csv('data/Assignment Task _ Dataset.csv' , index_col=False)
    df_sample = df_raw.sample(7)

    if request.method == "POST" and form.validate():
        session['op1'] = form.getOp1.data
        session['op2'] = form.getOp2.data

        

        return redirect(url_for('report'))

    return render_template('input.html',
                           df_html = df_sample.to_html(classes='table table-striped table-bordered'),
                           form = form)

@app.route("/report")
# generates the report and uses the library created by us
def report():
    return render_template('report.html')