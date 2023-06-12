from flask_restx import Namespace, Resource, fields
from app.apis.tasks.crud import add_task, get_tasks_by_user, task_completed
from app import bcrypt
from app.utils.utils import encode_auth_token
from flask import abort,session, request, current_app as app

tasks_namespace= Namespace("tasks")

task_resp_model= tasks_namespace.model("task", {
    "title": fields.String(required=True),
    "description": fields.String(required=True),
    "created_at": fields.String(required=True),
    "status": fields.String(required=True),
    "project_id": fields.Integer(required=True),"username": fields.String(required=True), "task_id":fields.Integer(required=True)
})
task_model=  tasks_namespace.model("task", {
    "title": fields.String(required=True),
    "description": fields.String(required=True),
   
    "project_id": fields.Integer(required=True),"username": fields.String(required=True), 
})
response_tasks_model= tasks_namespace.model("response_tasks_model", {"data":fields.List(fields.Nested(task_resp_model)), "message":fields.String(required=True)})

completed_response_model=tasks_namespace.model("completed_response_model",{"data":fields.String, "message":fields.String})
@tasks_namespace.route("/add-task")
class Task(Resource):
    @tasks_namespace.expect(task_model, validate=True)
    @tasks_namespace.response(200, "Task added successfully.")
    @tasks_namespace.response(400, "Please fill up all fields.")
    def post(self):
        try:
            data=request.get_json()
            title=data.get("title")
            description=data.get("description")
            username=data.get("username")
            project_id=data.get("project_id")
            if title and description  and project_id:
                add_task(title,description,project_id,username)
                return {"message":"Task added successfully."}, 200
            else:
                tasks_namespace.abort(400, "Please fill up all fields.")
        except Exception as e:
            return {"message":e}, 400
        
@tasks_namespace.route("/get-tasks")
class GetTaskList(Resource):
    @tasks_namespace.marshal_with(response_tasks_model)
    @tasks_namespace.response(200, "Task retrieved successfully.")
    @tasks_namespace.response(400, "Please fill up all fields.")

    def post(self):
        data=request.get_json()
        username=data.get("username")
        if username:
            resp=get_tasks_by_user(username)
            return {"message":"Tasks retrieved successfully.", "data":resp}, 200
        else:
            tasks_namespace.abort(400, "Please fill up all fields.")

@tasks_namespace.route("/complete-task")

class TaskCompleted(Resource):
    @tasks_namespace.marshal_with(completed_response_model)
    @tasks_namespace.response(200, "Task completed successfully.")
    @tasks_namespace.response(400, "Please fill up all fields.")

    def post(self):
        data=request.get_json()
        id=data.get("task_id")
        if id:
            resp=task_completed(id)
            return {"message":"Task completed successfully.", "data":resp}, 200
        else:
            tasks_namespace.abort(400, "Please fill up all fields.")


