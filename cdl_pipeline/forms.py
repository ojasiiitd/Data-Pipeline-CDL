from wtforms import Form , StringField , IntegerField , SubmitField , validators , SelectField , SelectMultipleField
from cdl_pipeline.pipeline_tasks import *

import os

class DataInputForm(Form) :
    # tasklist = [x for x in os.listdir("pipeline_tasks") if not x.startswith('__')]

    getOpt1 = SelectField("Task 1" , 
    choices=[x for x in os.listdir("pipeline_tasks") if not x.startswith('__')],
    validators=[validators.optional()]
    )
    getOpt2 = SelectField("Task 2" , 
    choices=[x for x in os.listdir("pipeline_tasks") if not x.startswith('__')],
    validators=[validators.optional()]
    )