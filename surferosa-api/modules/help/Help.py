from flask_restful import Resource
from flask_jwt_extended import (jwt_required, get_jwt_identity)

# classes
class Help(Resource):
    def get(self):
        return {"help": "this is the Surferosa api help"}, 200

