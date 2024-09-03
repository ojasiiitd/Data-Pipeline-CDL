from cdl_pipeline import app
from cdl_pipeline.forms import DataInputForm
from cdl_pipeline import logger
from .pipeline_tasks import *

from flask import render_template , flash , redirect , url_for , request , jsonify , session

import pandas as pd
import ast

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
        df_raw = pd.read_csv('cdl_pipeline/data/Assignment Task _ Dataset.csv' , index_col=False)
        df_sample = df_raw.sample(7)
        logger.info("Datafile read succeeded.")
    except FileNotFoundError:
        logger.error("The datafile is not available at the location.")
    except:
        logger.error("Datafile read failed.")

    if request.method == "POST" and form.validate():
        logger.info("Form validation successful, POST request sent.")

        logger.info("Reading form data.")
        
        # print(form.getOp1.data , form.col_op1.data)
        # print(form.getOp2.data , form.col_op2.data)

        cols_1 = eval(str(form.col_op1.data))
        cols_2 = eval(str(form.col_op2.data))

        session['op1'] = form.getOp1.data
        session['op2'] = form.getOp2.data
        session['col_op1'] = cols_1
        session['col_op2'] = cols_2

        logger.info("Form data read successful.")

        logger.info("Processing data.")

        tasklist = [(form.getOp1.data , cols_1),
                    (form.getOp2.data , cols_2)
                    ]
        
        for i,ops in enumerate(tasklist):
            session[f'report_op{i+1}'] = lib_map[ops[0]](df_raw , ops[1])

        return redirect(url_for('report'))

    return render_template('input.html',
                           df_html = df_sample.to_html(classes='table table-striped table-bordered'),
                           form = form
                           )

@app.route("/report")
# generates the report and uses the library created by us
def report():
    logger.info("Accessing the report endpoint.")
    report_1 = {
        'task': session.get('op1'),
        'cols': session.get('col_op1'),
        'result': session.get('report_op1')
    }
    report_2 = {
        'task': session.get('op2'),
        'cols': session.get('col_op2'),
        'result': session.get('report_op2')
    }

    op1_report = (report_1['task'] + "_report" , report_1['result'])
    op2_report = (report_2['task'] + "_report" , report_2['result'])

    reportlist = [op1_report,
                op2_report
                ]
    
    for_report = []

    for i,ops in enumerate(reportlist):
        for_report.append(lib_map[ops[0]](ops[1]))

    html_txt = {
        'missing_vals': 'Missing Values Processing',
        'dup_vals': 'Duplicate Values Processing',
    }

    print(for_report[1])

    return render_template('report.html',
                           report_1 = report_1,
                           report_2 = report_2,

                           task1 = html_txt[report_1['task']],
                           task2 = html_txt[report_2['task']],

                           report_content = for_report
                           )