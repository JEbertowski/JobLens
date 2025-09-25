from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()


    app = Flask(
        __name__,
        static_folder="../static",
        template_folder="templates"
    )


    app.config.from_object("config.Config")


    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
