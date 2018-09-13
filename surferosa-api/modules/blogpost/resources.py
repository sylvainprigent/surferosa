from flask import Blueprint
from flask_restful import Api
from modules.blogpost.Blogpost import BlogpostCollection, Blogpost

# routes
api_blogpost = Blueprint('blogpost', __name__)
api = Api(api_blogpost)

api.add_resource(BlogpostCollection, '/')
api.add_resource(Blogpost, '/<string:id>')