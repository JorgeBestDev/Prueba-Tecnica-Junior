from flask import Flask
from flask_sqlalchemy  import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    register_blueprints(app)

    return app

def register_blueprints(app):
    from app.routes import (producto_routes, categoria_routes)
    app.register_blueprint(producto_routes.bp)
    app.register_blueprint(categoria_routes.bp)