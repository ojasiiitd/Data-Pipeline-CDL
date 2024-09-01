from flask import Flask

app = Flask(__name__)
app.secret_key = 'cdl_secret_key'

from cdl_pipeline import routes