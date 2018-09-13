import os

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
# MONGO_URI = "mongodb://" + os.environ.get('MONGO_URI')
MONGO_URI = "mongodb://surferosa-database:27017/surferosa"
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')