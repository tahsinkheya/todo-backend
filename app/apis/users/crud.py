from app import mongo
import uuid
from datetime import datetime

db=mongo.db
users=db['users']

def get_all_users():
    return list(users.find({}).sort('created_at',-1)) #-1 sorts stuff in descending order

def get_user_by_username(username):
    return users.find_one({"username":username})

def signup(username,first_name, last_name, hash_password):

    return users.insert_one({
        "username":username, "first_name":first_name, "last_name":last_name, "password":hash_password
    })

def get_user_count_by_username(username):
    return users.count_documents({"username": username})