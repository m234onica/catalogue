from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

from src.route.api import api
from src.route.blog import blog
from src.login.auth import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(api)
    app.register_blueprint(blog)
    app.register_blueprint(auth)    
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    return app
