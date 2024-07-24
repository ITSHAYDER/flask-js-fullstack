from flask_restful import Resource
from flask import request
from .models import db, User
from werkzeug.security import check_password_hash, generate_password_hash

class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {'message': 'Email and password are required'}, 400

        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            return {'message': 'Login successful'}, 200
        else:
            return {'message': 'Invalid email or password'}, 401

class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return {'message': 'Email and password are required'}, 400

        if User.query.filter_by(email=email).first():
            return {'message': 'User already exists'}, 400

        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201
