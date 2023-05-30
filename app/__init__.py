from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import os
mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app_settings = os.environ.get(
        "APP_SETTINGS", "app.config.BaseConfig")
    app.config.from_object(app_settings)
    mongo.init_app(app)
    bcrypt.init_app(app)
    with app.app_context():
        from app.apis import api
        api.init_app(app)
    

    return app