from flask_restx import Namespace, Resource, fields
from app.apis.userInfo.crud import get_user_info
from app.apis.decorator import token_required
from app.utils.utils import encode_auth_token
from flask import abort, request, current_app as app, session

user_info_namespace= Namespace("user_info")
user_info_model= user_info_namespace.model("user_info", {
    "first_name": fields.String(required=True),
    "last_name": fields.String(required=True),
})

get_user_model= user_info_namespace.model("get_user_model",{"data":fields.Nested(user_info_model), "message":fields.String(required=True)})

@user_info_namespace.route("/get-user-info")
class UserInfo(Resource):
    @token_required
    @user_info_namespace.marshal_with(get_user_model)
    @user_info_namespace.response(200, "Retrieved user information successfully")
    @user_info_namespace.response(400, "This user doest exist")
    def post(self):
        try:
            data=request.get_json()
            app.logger.info(data)
            username=data.get("username")
            response= get_user_info(username)
            if response is None:
                user_info_namespace.abort(400, "This user doest exist")
            else:
                respObj={"data":response, "message":"Retrieved user information successfully"}
                return respObj
        except Exception as e:
            user_info_namespace.abort(400, e)


    

    