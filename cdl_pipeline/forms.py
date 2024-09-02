from wtforms import Form , StringField , IntegerField , TextAreaField, SubmitField , validators , SelectField , SelectMultipleField

class DataInputForm(Form) :
    choices = [("missing_vals" , "Missing Values") , ("dup_vals" , "Duplicate Values")]

    getOp1 = SelectField("Task 1" , 
    choices=choices,
    validators=[validators.DataRequired()]
    )
    col_op1 = TextAreaField('Dictionary/List for Task 1', validators=[validators.DataRequired()])
    
    getOp2 = SelectField("Task 2" , 
    choices=choices,
    validators=[validators.DataRequired()]
    )
    col_op2 = TextAreaField('Dictionary/List for Task 2', validators=[validators.DataRequired()])
