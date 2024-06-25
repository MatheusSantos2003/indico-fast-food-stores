from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from extensions.routes_extension import register_routes
from extensions.exception_extension import register_exception_handler
from werkzeug.exceptions import HTTPException
from models import db


def create_app():
    UPLOAD_FOLDER = '/path/to/the/uploads'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}    

    app = Flask(__name__,template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stores.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)

    migrate = Migrate(app, db)

    register_routes(app)
    register_exception_handler(app)

    return app
