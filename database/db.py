import os

# import redis
# from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

# mongoDB
# mongo_host = os.environ.get("MONGO_HOST", "")
# mongo_db_name = os.environ.get("MONGO_DB_NAME", "")
# mongo_db = MongoEngine()

"""
memSQL_DB & mySQL_DB connection 
"""
mem_db = SQLAlchemy()
mysql_db_string = os.environ.get("MYSQL_CONNECTION", "")
print('mysql_db_string', mysql_db_string)
SQLALCHEMY_BINDS = {
    "mysql": mysql_db_string,
    # "memsql": mem_db_string
}
#SQLALCHEMY_BINDS = {
#    "mysql": {
#        "uri": mysql_db_string,
#        "ssl": DISABLED
#    }
#}
"""
Elasticsearch connection commented for now
if you want to enable, Need to install pip install Elasticsearch
"""

# redis
# REDIS_HOST = os.environ.get("REDIS_HOST", None)
# REDIS_PORT = os.environ.get("REDIS_PORT", None)
# redis_db = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf-8", decode_responses=True)


def initialize_db(app):
    # MongoDB
    # app.config["MONGODB_HOST"] = mongo_host
    # app.config["MONGODB_DATABASE"] = mongo_db_name
    # mongo_db.init_app(app)

    # mysql
    app.config["SQLALCHEMY_DATABASE_URI"] = mysql_db_string
    app.config["SQLALCHEMY_BINDS"] = SQLALCHEMY_BINDS
    app.config["SQLALCHEMY_POOL_SIZE"] = 150
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    mem_db.init_app(app=app)

    # MEMSQL Migrate
    Migrate(app, mem_db)

    @app.before_request
    def create_tables():
        mem_db.create_all()


# def connect_redis():
#     return redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
