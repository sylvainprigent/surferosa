from flask import Flask
from database import mongo
from modules.auth.jwt import jwt

# app
app = Flask(__name__)
app.config.from_object("config")

# database
mongo.init_app(app)
# mongo.db.users.remove()
# mongo.db.users.insert_one({'username': "pbismut", 'name': "Bismut", 'firstname': "Paul", "email": "paul.bismut@mail.com"})

# jwt auth
jwt.init_app(app)

# modules
from modules.auth.resources import api_auth
app.register_blueprint(api_auth, url_prefix='/api/v1/auth')

from modules.user.resources import api_user
app.register_blueprint(api_user, url_prefix='/api/v1/users')

from modules.help.resources import api_help
app.register_blueprint(api_help, url_prefix='/api/v1/help')

from modules.blogpost.resources import api_blogpost
app.register_blueprint(api_blogpost, url_prefix='/api/v1/blogpost')

from modules.news.resources import api_news
app.register_blueprint(api_news, url_prefix='/api/v1/news')


# start app
if __name__ == "__main__":
    app.run("0.0.0.0", port=80, debug=True);
