from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
from .routes import register_routes

db = SQLAlchemy()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cors.init_app(app)

    register_routes(app)

    # 👇 CREATE TABLES HERE
    with app.app_context():
        from app.models import User, Ticket
        db.create_all()
        print("✅ Database tables created")

    return app
