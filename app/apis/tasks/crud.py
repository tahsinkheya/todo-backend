from app import mongo
import time

from datetime import datetime

db=mongo.db
tasks=db['tasks']
def add_task(title,description,project_id, username):
        payload={"created_at": datetime.utcnow(),"task_id":int(time.time() * 1000) , "status":"open","title":title,"username":username,"description":description,"project_id":project_id}
        return tasks.insert_one(payload)

def get_tasks_by_user(username):
        return list(tasks.find({"username":username}).sort("created_at",-1))


def task_completed( task_id):
         return tasks.update_one({'task_id':task_id},{"$set":{"status":"close", "done_at":datetime.utcnow() }})




