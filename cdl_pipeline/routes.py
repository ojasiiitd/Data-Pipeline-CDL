from cdl_pipeline import app
from cdl_pipeline.forms import DataInputForm
from cdl_pipeline import logger

from flask import render_template , flash , redirect , url_for , request , jsonify , session

import pandas as pd

@app.route("/")
# homepage where the root endpoint points to
def homepage():
    logger.info("Accessing homepage endpoint.")
    return render_template("information.html")

@app.route("/input" , methods = ['GET' , 'POST'])
# user proivides the sequential input using a form here, and also sees the dataset
def inputData():
    logger.info("Accessing input form endpoint.")
    form = DataInputForm(request.form)

    try:
        logger.info("Reading datafile.")
        df_raw = pd.read_csv('data/Assignment Task _ Dataset.csv' , index_col=False)
        df_sample = df_raw.sample(7)
        logger.info("Datafile read succeeded.")
    except FileNotFoundError:
        logger.error("The datafile is not available at the location.")
    except:
        logger.error("Datafile read failed.")

    if request.method == "POST" and form.validate():
        logger.info("Form validation successful, POST request sent.")

        try:
            logger.info("Reading form data.")
            session['op1'] = form.getOp1.data
            session['op2'] = form.getOp2.data
            logger.info("Form data read successful.")
        except:
            logger.error("Form data read failed.")

        logger.info("Processing data.")

        return redirect(url_for('report'))

    return render_template('input.html',
                           df_html = df_sample.to_html(classes='table table-striped table-bordered'),
                           form = form)

@app.route("/report")
# generates the report and uses the library created by us
def report():
    logger.info("Accessing the report endpoint.")
    return render_template('report.html')