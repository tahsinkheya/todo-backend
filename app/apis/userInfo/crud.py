from app import mongo
from flask import session
from datetime import datetime
from flask import current_app as app

db=mongo.db
users=db['users']

def get_user_info(username):
    app.logger.info(username)
    return users.find_one({"username":username}, {"first_name":1,"last_name":1})
