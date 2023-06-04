from flask_restx import Api

from app.apis.users.api import users_namespace
from app.apis.project.api import project_namespace
from app.apis.ping.alive import alive_namespace

api = Api(version="1.0", title="todo app docs", doc="/docs" ,prefix="/api/v1")

api.add_namespace(alive_namespace, path="")
api.add_namespace(project_namespace, path="")
api.add_namespace(users_namespace, path="")
