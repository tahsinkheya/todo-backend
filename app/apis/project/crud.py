from app import mongo
from datetime import datetime

db=mongo.db
projects=db['projects']

def add_project(name):
    projects.insert_one({
        "name":name, "created_at":datetime.utcnow()
    })

