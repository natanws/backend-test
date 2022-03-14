from flask import Flask
from app.views.user_blueprint import bp_user

def init_app(app:Flask):
    app.register_blueprint(bp_user)