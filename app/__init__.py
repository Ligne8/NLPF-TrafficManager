from flask import Flask
from flask_pymongo import PyMongo
from app.main import main as main_bp

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    mongo = PyMongo(app)

    #registering blueprints
    app.register_blueprint(main_bp)

    @app.route("/hello")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app


create_app()