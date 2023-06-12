from app import mongo
from datetime import datetime
import time

db=mongo.db
projects=db['projects']

def add_project(name, description, username):
    projects.insert_one({"username":username,
        "name":name, "created_at":datetime.utcnow(), "description":description, "project_id":int(time.time() * 1000) 
    })

def get_project_by_user_id(username):
        return list(projects.find({"username":username}).sort("created_at",-1))
