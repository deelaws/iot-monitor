from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from mod_app.config import config_map

db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_message = 'Successful login'
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in #todo localization'

def create_app(config_name):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    app.config.from_object(config_map[config_name])

    config_map[config_name].init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Register Blueprints

    @app.route("/")
    def hello():
        return "Hello World"

    print(app.url_map)
    
    return app