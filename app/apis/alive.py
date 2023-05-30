from flask_restx import Namespace, Resource, fields


alive_namespace=Namespace("ping")

respon= alive_namespace.model ("alive", {"status": fields.String(required=True), "message":fields.String(required=True)})

class Alive(Resource):
    @alive_namespace.marshal_with(respon)
    @alive_namespace.response(200, "Alive")
    def get(self):
        response = {}
        response['status']= "success"
        response['message']= "Alive"
        return response, 200
    
alive_namespace.add_resource( Alive, "")