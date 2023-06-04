from flask_restx import Namespace, Resource, fields
from app.apis.users.crud import get_user_count_by_username,signup,get_user_by_username
from app import bcrypt
from app.utils.utils import encode_auth_token
from flask import abort, request, current_app as app

users_namespace= Namespace("users")

user_model= users_namespace.model("user", {
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
    "username": fields.String(required=True),
    "password": fields.String(required=True),
})

user_login_model= users_namespace.model("user_login_model", {
    "username": fields.String(required=True),
    "password": fields.String(required=True),
})

user_login_model_response= users_namespace.model("user_login_model_response", {
    "message": fields.String(required=True),
    "auth_token": fields.String(required=True),
})

@users_namespace.route("/signup")
class Signup(Resource):
    @users_namespace.expect(user_model, validate=True)
    @users_namespace.response(200, "User signed up successfully.")
    @users_namespace.response(400, "PLease fill up all fields.")
    @users_namespace.response(409, "User with this username already exists.")
    def post(self):
        try:
            data=request.get_json()
            app.logger.info(data)
            fname=data.get("first_name")
            lname=data.get("last_name")
            username=data.get("username")
            password=data.get("password")
            if fname and lname and username and password:
                if get_user_count_by_username(username)<=0:
                    hashed_password= bcrypt.generate_password_hash(password,13).decode()
                    signup(username,fname, lname, hashed_password)
                    return {"message":"User signed up successfully"}, 200
                else:
                    users_namespace.abort(409, f"User with this username already exists.")
            else:
                users_namespace.abort(400, f"Please fill up all fields.")
        except Exception as e:
            return {"message":e}, 400

@users_namespace.route("/login")
class Login(Resource):
    @users_namespace.marshal_with(user_login_model_response)
    @users_namespace.expect(user_login_model)
    @users_namespace.response(200, "Login successfull.")
    @users_namespace.response(400, "PLease fill up all fields.")
    @users_namespace.response(401, "Wrong password")
    @users_namespace.response(400, "User doesn't exist")
    def post(self):
        data=request.get_json()
        username=data.get('username')
        password=data.get('password')
        if username and password:
            user=get_user_by_username(username)
            if user:
                is_valid= bcrypt.check_password_hash(user['password'], password)
                if is_valid:
                    auth_token= encode_auth_token(username)
                    responseObject = {
                        "auth_token": auth_token,
                        "message": "Logged in successfully!"
                    }
                    return responseObject, 200
                else:
                    users_namespace.abort(401, "Wrong password")
            else:
                users_namespace.abort(400, "User doesn't exist")
        else:
            users_namespace.abort(400, "PLease fill up all fields.")


# users_namespace.add_resource(Login, "/login")
# users_namespace.add_resource(Signup, "/signup")

