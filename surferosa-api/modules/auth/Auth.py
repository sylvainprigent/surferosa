from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import  create_access_token, create_refresh_token
from passlib.hash import pbkdf2_sha256
from database import mongo

# classes
class Auth(Resource):
    def post(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username:
            return {"msg": "Missing username parameter"}, 400
        if not password:
            return {"msg": "Missing password parameter"}, 400

        user = mongo.db.users.find_one({"username": username})
        if user:
            if pbkdf2_sha256.verify(password, user["password"]):
                data = {
                    "username": username,
                    'access_token': create_access_token(identity=username),
                    'refresh_token': create_refresh_token(identity=username)
                }
                return data, 200
            else:
                return {"msg": "Password incorrect"}, 400
        else:
            return {"msg": "User not found"}, 400



