from flask import Flask
from flask_restful import reqparse, Api


from app.controllers.containerController import ContainerController

app = Flask(__name__)
parser = reqparse.RequestParser()
parser.add_argument('container')

api = Api(app)
api.add_resource(ContainerController, '/runcontainer')

if __name__ == "__main__":
    app.run(port=7500)
