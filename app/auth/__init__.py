from flask import Blueprint

# Basically blueprints are subset of your app that has some part handled, like different domains, for example errors auth and etc...
bp = Blueprint('auth', __name__)

from app.auth import routes