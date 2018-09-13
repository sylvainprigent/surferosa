from flask import Blueprint
from flask_restful import Api
from modules.news.news import NewsCollection, News

# routes
api_news = Blueprint('news', __name__)
api = Api(api_news)

api.add_resource(NewsCollection, '/')
api.add_resource(News, '/<string:id>')