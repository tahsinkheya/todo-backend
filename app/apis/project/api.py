from flask_restx import Namespace, Resource, fields
from flask import request, current_app as app
from app.apis.project.crud import get_project_by_user_id, add_project
from app import bcrypt
from app.apis.project.crud import add_project
from app.apis.decorator import token_required

project_namespace= Namespace("projects")

project_model=project_namespace.model('project', {"project_name":fields.String(required=True),"username":fields.String(required=True),
"project_desc":fields.String(required=True)})


project_row=project_namespace.model('project_row', {"name":fields.String(required=True),"created_at":fields.String(required=True),"description":fields.String(required=True),"username":fields.String(required=True),"project_id":fields.Integer})

response_project_model= project_namespace.model("response_project_model", {"data":fields.List(fields.Nested(project_row)), "message":fields.String(required=True)})

request_project_model= project_namespace.model("request_project_model", {"username":fields.String(required=True)})

@project_namespace.route("/add-project")
class Project(Resource):
    @token_required
    @project_namespace.expect(project_model, validate=True)
    @project_namespace.response(200, "Project added successfully.")
    @project_namespace.response(400, "Please fill up all fields.")
    def post (self):
        try:
            data=request.get_json()
            name= data.get("project_name")
            desc= data.get("project_desc")
            username= data.get("username")
            if name and desc and username:
                add_project(name,desc, username)
                return {"message":"Project added successfully."}, 200

            else:
                project_namespace.abort(400, "PLease fill up all fields.")
        except Exception as e:
            return {"message":e}, 200
        
@project_namespace.route("/get-projects")

class GetProjectList(Resource):
    @token_required
    @project_namespace.marshal_with(response_project_model)
    @project_namespace.expect(request_project_model, validate=True)
    @project_namespace.response(200, "Project retrieved successfully.")
    @project_namespace.response(400, "Please fill up all fields.")
    def post(self):
        data=request.get_json()
        username=data.get("username")
        app.logger.info("-----------------------------------------------")
        app.logger.info(username)
        app.logger.info("-----------------------------------------------")

        if username :
            resp=get_project_by_user_id(username)
            return {"message":"Projects retrieved successfully.","data":resp}, 200
        else:
            project_namespace.abort(400, "Please fill up all fields.")



   