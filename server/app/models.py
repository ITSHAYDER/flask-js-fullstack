from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    email = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
