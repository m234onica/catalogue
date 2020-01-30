from flask import Flask

from src.route.api import api
from src.route.blog import blog


def create_app():
  app = Flask(__name__)
  app.config.from_object('config')

  app.register_blueprint(api)
  app.register_blueprint(blog)

  return app
