from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from .models import db
from .config import Config
from .resources import LoginResource, RegisterResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create the database tables

    # Initialize CORS
    CORS(app)

    api = Api(app)
    api.add_resource(LoginResource, '/api/login')
    api.add_resource(RegisterResource, '/api/register')

    return app
