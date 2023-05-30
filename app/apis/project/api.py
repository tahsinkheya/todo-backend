from flask_restx import Namespace, Resource, fields
from flask import request
from app.apis.users.crud import get_user_count_by_username,signup,get_user_by_username
from app import bcrypt
from app.apis.project.crud import add_project

project_namespace= Namespace("projects")

project_model=project_namespace.model('project', {"project_name":fields.String(required=True), "id":fields.Integer(readonly=True, description="db generated id")})

class Project(Resource):
    @project_namespace.expect(project_model, validate=True)
    @project_namespace.response(200, "Project added successfully.")
    @project_namespace.response(400, "PLease fill up all fields.")
    def post (self):
        try:
            data=request.get_json()
            name= data.get("name")
            if name:
                add_project(name)
                return {"message":"Project added successfully."}, 200

            else:
                project_namespace.abort(400, "PLease fill up all fields.")
        except Exception as e:
            return {"message":e}, 200

   