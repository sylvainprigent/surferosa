from flask_restful import Resource
from flask import request, json
from marshmallow import Schema, fields, ValidationError
from database import mongo
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId
import datetime


# parser
class BlogpostSchema(Schema):
    username = fields.Str(required=False)
    content = fields.Str(required=True)
    created = fields.DateTime(required=False)
    modified = fields.DateTime(required=False)


blogpost_schema = BlogpostSchema(strict=True)


# classes
class BlogpostCollection(Resource):
    @jwt_required
    def get(self):
        data = mongo.db.blogposts
        output = []
        for d in data.find():
            output.append({"_id": str(d["_id"]),
                           "username": d["username"],
                           "content": d["content"],
                           "created": str(d["created"]),
                           "modified": str(d["modified"]),
                           })
        return (output)

    @jwt_required
    def post(self):
        json_input = request.get_json()
        try:
            blogpost_schema.load(json_input)
        except ValidationError as err:
                return (json.dumps({"message": err.messages})), 422

        blogpost_id = mongo.db.blogposts.insert_one({'username': get_jwt_identity(),
                                                     'content': json_input["content"],
                                                     "created": datetime.datetime.utcnow(),
                                                     "modified": datetime.datetime.utcnow()
                                                 }).inserted_id

        output = {"message": "user added", "id": str(blogpost_id), "data": json_input};
        return (output), 201


class Blogpost(Resource):
    @jwt_required
    def get(self, id):
        data = mongo.db.blogposts.find_one({'_id': ObjectId(id)})
        if data:
            return ({'_id': str(data["_id"]),
                    'username': data["username"],
                    'content': data["content"],
                    "created": str(data["created"]),
                    "modified": str(data["modified"])
                    })
        else:
            return ({'result': "No such post"})

    @jwt_required
    def put(self, id):
        json_input = request.get_json()
        data = mongo.db.blogposts.find_one({'_id': ObjectId(id)})
        if data:
            try:
                blogpost_schema.load(json_input)
            except ValidationError as err:
                return (json.dumps({"message": err.messages})), 422

            data["username"] = get_jwt_identity();
            data["content"] = json_input["content"];
            data["modified"] = datetime.datetime.utcnow()
            mongo.db.blogposts.save(data)
            return ({'_id': str(data["_id"]),
                    'username': data["username"],
                    'content': data["content"],
                    "created": str(data["created"]),
                    "modified": str(data["modified"])
                    })
        else:
            return ({'result': "No such post"})

    @jwt_required
    def delete(self, id):
        data = mongo.db.blogposts.find_one({'_id': ObjectId(id)})
        if data:
            mongo.db.blogposts.remove(data)

        return ({"message": "Deleted"}), 204
