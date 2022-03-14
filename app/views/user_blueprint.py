from flask import Blueprint

from app.controllers.user_controller import create_user, get_all

bp_user = Blueprint('bp_user', __name__, url_prefix='/user')
bp_user.get('')(get_all)
bp_user.post('')(create_user)