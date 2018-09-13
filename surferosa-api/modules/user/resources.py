from flask import Blueprint
from flask_restful import Api
from modules.user.User import UserCollection, User

# routes
api_user = Blueprint('user', __name__)
api = Api(api_user)

api.add_resource(UserCollection, '/')
api.add_resource(User, '/<string:username>')