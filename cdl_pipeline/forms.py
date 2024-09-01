from wtforms import Form , StringField , IntegerField , SubmitField , validators , SelectField , SelectMultipleField
from cdl_pipeline.pipeline_tasks import *

import os

class DataInputForm(Form) :
    choices = [(x , x[:-3]) for x in os.listdir("pipeline_tasks") if not x.startswith('__')]

    getOp1 = SelectField("Task 1" , 
    choices=choices,
    validators=[validators.optional()]
    )
    getOp2 = SelectField("Task 2" , 
    choices=choices,
    validators=[validators.optional()]
    )