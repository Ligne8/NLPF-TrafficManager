import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    MONGO_DB_URI = os.environ.get('DATABASE_URL') or 'mongodb://localhost:27017/myDatabase'