from flask import Flask
import logging

app = Flask(__name__)
app.secret_key = 'cdl_secret_key'

logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)


from cdl_pipeline import routes