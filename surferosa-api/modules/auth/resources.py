from flask import Blueprint
from flask_restful import Api
from modules.auth.Auth import Auth
from modules.auth.Refresh import Refresh

api_auth = Blueprint('auth', __name__)
api = Api(api_auth)

api.add_resource(Auth, '/')
api.add_resource(Refresh, '/refresh')
