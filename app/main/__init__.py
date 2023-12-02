from flask import Blueprint

# blueprint for main application logic
bp = Blueprint('main', __name__)

from app.main import routes