from flask_jwt_extended import (
    create_access_token, get_jwt_identity
)

class JwtServices(object):
    @staticmethod
    def tokenify(data):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return { "jwt": access_token, "data": data}