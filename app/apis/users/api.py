from flask_restx import Namespace, Resource, fields
from flask import request
from app.apis.users.crud import get_user_count_by_username,signup
from app import bcrypt
users_namespace= Namespace("users")

user_model= users_namespace.model("user", {
    "first_name": fields.String(required=False),
    "last_name": fields.String(required=False),
    "username": fields.String(required=False),
    "password": fields.String(required=False),
})

user_login_model= users_namespace.model("user", {
    "username": fields.String(required=False),
    "password": fields.String(required=False),
})


class Signup(Resource):
    @users_namespace.expect(user_model, validate=True)
    @users_namespace.response(200, "User signed up successfully.")
    @users_namespace.response(400, "PLease fill up all fields.")
    @users_namespace.response(409, "User with this username already exists.")
    def post(self):
        data=request.get_json()
        fname=data.get("first_name")
        lname=data.get("last_name")
        username=data.get("username")
        password=data.get("password")
        if fname and lname and username and password:
            if get_user_count_by_username(username):
               hashed_password= bcrypt.generate_password_hash(password,13).decode()
               signup(username,fname, lname, hashed_password)
               return {"message":"User signed up successfully"}, 200
            else:
                users_namespace.abort(409, f"User with this username already exists.")

        else:
            users_namespace.abort(400, f"PLease fill up all fields.")
