from flask import Flask

app = Flask(__name__)
app.config.from_object('config_DEBUG')

from app import views
