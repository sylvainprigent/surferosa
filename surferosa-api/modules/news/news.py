from flask_restful import Resource
from flask import request, json, jsonify
from marshmallow import Schema, fields, ValidationError
from database import mongo
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
import datetime
from modules.auth.JwtServices import JwtServices


# parser
class NewSchema(Schema):
    username = fields.Str(required=False)
    content = fields.Str(required=True)
    created = fields.DateTime(required=False)
    modified = fields.DateTime(required=False)


news_schema = NewSchema(strict=True)


# classes
class NewsCollection(Resource):

    def get(self):
        data = mongo.db.news
        output = []
        for d in data.find():
            output.append({"_id": str(d["_id"]),
                           "username": d["username"],
                           "content": d["content"],
                           "created": str(d["created"]),
                           "modified": str(d["modified"]),
                           })
        return output

    def post(self):
        json_input = request.get_json()
        try:
            news_schema.load(json_input)
        except ValidationError as err:
                return json.dumps({"message": err.messages}), 422

        news_id = mongo.db.news.insert_one({'username': "Default user name",
                                                     'content': json_input["content"],
                                                     "created": datetime.datetime.utcnow(),
                                                     "modified": datetime.datetime.utcnow()
                                                 }).inserted_id

        output = {"message": "user added", "id": str(news_id), "data": json_input};
        return output, 201


class News(Resource):
    
    def get(self, id):
        data = mongo.db.news.find_one({'_id': ObjectId(id)})
        if data:
            return JwtServices.tokenify({'_id': str(data["_id"]),
                    'username': data["username"],
                    'content': data["content"],
                    "created": str(data["created"]),
                    "modified": str(data["modified"])
                    })
        else:
            return {'result': "No such post"}

    @jwt_required
    def put(self, id):
        json_input = request.get_json()
        data = mongo.db.news.find_one({'_id': ObjectId(id)})
        if data:
            try:
                news_schema.load(json_input)
            except ValidationError as err:
                return json.dumps({"message": err.messages}), 422

            data["username"] = get_jwt_identity();
            data["content"] = json_input["content"];
            data["modified"] = datetime.datetime.utcnow()
            mongo.db.news.save(data)
            return {'_id': str(data["_id"]),
                    'username': data["username"],
                    'content': data["content"],
                    "created": str(data["created"]),
                    "modified": str(data["modified"])
                    }
        else:
            return {'result': "No such post"}

    @jwt_required
    def delete(self, id):
        data = mongo.db.news.find_one({'_id': ObjectId(id)})
        if data:
            mongo.db.news.remove(data)

        return {"message": "Deleted"}, 204
