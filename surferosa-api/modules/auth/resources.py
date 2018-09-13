from flask import Blueprint
from flask_restful import Api
from modules.auth.Auth import Auth

api_auth = Blueprint('auth', __name__)
api = Api(api_auth)

api.add_resource(Auth, '/')