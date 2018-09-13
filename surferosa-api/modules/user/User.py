from flask_restful import Resource
from flask import request, json, jsonify
from marshmallow import Schema, fields, ValidationError
from database import mongo
from passlib.hash import pbkdf2_sha256
import json

# parser
class UserSchema(Schema):
    username = fields.Str(required=True)
    name = fields.Str(required=True)
    firstname = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=False)


user_schema = UserSchema(strict=True)

# classes
class UserCollection(Resource):
    def get(self):
        users = mongo.db.users
        output = []
        for s in users.find():
            output.append({"username": s["username"],
                           "name": s["name"],
                           "firstname": s["firstname"],
                           "email": s["email"],
                           "password": s["password"]})
        return {'result': output}

    def post(self):
        json_input = request.get_json()
        user = mongo.db.users.find_one({"username": json_input["username"]})
        if user:
            return {"msg": "User already exists"}, 400
        else:
            try:
                user_schema.load(json_input)
            except ValidationError as err:
                return json.dumps({"message": err.messages}), 422

            password = request.json.get('password', None)
            if not password:
                return {"msg": "Missing password parameter"}, 400

            hashh = pbkdf2_sha256.encrypt(json_input["password"], rounds=200000, salt_size=16)

            user_id = mongo.db.users.insert_one({'username': json_input["username"],
                                                 'name': json_input["name"],
                                                 'firstname': json_input["firstname"],
                                                 "email": json_input["email"],
                                                 "password": hashh,
                                                 }).inserted_id

            return {"message": "user added", "id": str(user_id), "data": json_input}, 201


class User(Resource):
    def get(self, username):
        user = mongo.db.users.find_one({"username": username})
        if user:
            return {'username': user["username"],
                    'name': user["name"],
                    'firstname': user["firstname"],
                    "email": user["email"]
                    }
        else:
            return jsonify({'result': "No such user"})

    def put(self, username):
        json_input = request.get_json()
        user = mongo.db.users.find_one({"username": username})
        if user:
            try:
                data = user_schema.load(json_input)
            except ValidationError as err:
                return json.dumps({"message": err.messages}), 422

            user["name"] = json_input["name"];
            user["firstname"] = json_input["firstname"];
            user["email"] = json_input["email"];
            mongo.db.users.save(user)
        return data

    def delete(self, username):
        user = mongo.db.users.find_one({"username": username})
        if user:
            mongo.db.users.remove(user)

        return {"message": "Deleted"}, 204
