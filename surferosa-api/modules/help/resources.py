from flask import Blueprint
from flask_restful import Api
from modules.help.Help import Help

api_help = Blueprint('help', __name__)
api = Api(api_help)

api.add_resource(Help, '/')