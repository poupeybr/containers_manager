from flask_restful import Resource, request
from app.models.container import Container
from app.services.containerService import ContainerService
from flask_restful import abort
from os import environ 


class ContainerController(Resource):
    def __init__(self):
        self.containerService = ContainerService()

    def post(self):
        print(request) 
        print(request.authorization) 
        print(request.get_json())             
        auth = request.headers.get('Authorization')
        
        if not auth:
            abort(401, message="Not Authorized")
            
        jwt = auth.split('Bearer ')[1]
        
        auth_key_expected = environ.get('AUTH_KEY')
        
        if jwt != auth_key_expected:
            abort(401, message="Not Authorized")
             
        data = request.get_json()
        
        try:
            self.containerService.runcontainer(data)

            return {
                "message": "Success"
            }
        except Exception as e:
            abort(500, message=e)
        
    def map_to_object(self, data, obj_class):
        return obj_class(**data)

        
        
