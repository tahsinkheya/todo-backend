from app import mongo
from flask import session
from datetime import datetime

db=mongo.db
users=db['users']

def get_user_info():
    username=session.get('username')
    return list(users.find_one({"username":username}))
