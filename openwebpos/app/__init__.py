import os

from flask import Flask, current_app

from openwebpos.app import config
from openwebpos.blueprints import blueprints
from openwebpos.utils.jinja2 import template_filters


def create_app(config_filename=None, config_path=None):
    app = Flask(
        __name__,
        template_folder="ui/templates",
        static_folder="ui/static",
        instance_relative_config=True,
        instance_path=config_path,
    )

    # Default configuration settings
    app.config.from_object(config)

    # User configuration settings
    if config_filename:
        app.config.from_pyfile(config_filename, silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register template filters
    template_filters(app)

    # Load extensions
    load_extensions(app)

    # Register blueprints
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    @app.route("/")
    def index():
        test = current_app.config["TEST"]
        return f"Hello, World! {test}"

    return app


def load_extensions(app):
    from openwebpos.app.extensions import db, login_manager, csrf

    csrf.init_app(app)

    # Initialize extensions if the database is configured
    db.init_app(app)

    # Create all tables
    with app.app_context():
        db.create_all()

        login_manager.init_app(app)
        login_manager.login_view = "user.login"

        def get_user_by_id(user_id):
            from openwebpos.blueprints.user.models.UserModel import User

            return User.query.get(user_id)

        @login_manager.user_loader
        def load_user(user_id):
            return get_user_by_id(user_id)
