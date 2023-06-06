from app import mongo
import uuid
from datetime import datetime

db=mongo.db
tasks=db['tasks']
def add_task(title,description,due_date,project_id):
        payload={"created_at": datetime.utcnow(), "title":title,"description":description,"due_date":due_date,"project_id":project_id}
        return tasks.insert_one(payload)

