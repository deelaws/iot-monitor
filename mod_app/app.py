from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from mod_app.config import config_map

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

    app.config.from_object(config_map[config_name])

    config_map[config_name].init_app(app)
    db.init_app(app)

    # Register Blueprints
    from mod_sensor.views import mod_sensor
    from mod_sensor.exceptions import InvalidInput
    app.register_blueprint(mod_sensor)

    @app.route("/")
    def hello():
        return "Hello World"

    @app.errorhandler(InvalidInput)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    #print(app.url_map)

    return app
