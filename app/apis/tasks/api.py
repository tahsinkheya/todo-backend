from flask_restx import Namespace, Resource, fields
from app.apis.users.crud import add_task
from app import bcrypt
from app.utils.utils import encode_auth_token
from flask import abort,session, request, current_app as app

tasks_namespace= Namespace("tasks")

task_model= tasks_namespace.model("user", {
    "title": fields.String(required=True),
    "description": fields.String(required=True),
    "due_date": fields.String(required=True),
    "project_id": fields.String(required=True),
})

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
            due_date=data.get("due_date")
            project_id=data.get("project_id")
            if title and description and due_date and project_id:
                add_task(title,description,due_date,project_id)
                return {"message":"Task added successfully."}, 200
            else:
                tasks_namespace.abort(400, "Please fill up all fields.")
        except Exception as e:
            return {"message":e}, 400
