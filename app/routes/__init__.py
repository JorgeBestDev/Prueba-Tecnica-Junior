from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import producto_routes, categoria_routes