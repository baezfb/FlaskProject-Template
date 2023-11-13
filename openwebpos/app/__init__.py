import os

from flask import Flask

from openwebpos.app import config


def create_app(config_filename=None):
    app = Flask(
        __name__,
        template_folder="ui/templates",
        static_folder="ui/static",
        instance_relative_config=True,
    )

    app.config.from_object(config)
    if config_filename is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the config file if passed in
        app.config.from_mapping(config_filename)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    load_extensions(app)

    @app.route("/")
    def index():
        return "Hello, World!"

    return app


def load_extensions(app):
    from openwebpos.app.extensions import db, login_manager, csrf

    csrf.init_app(app)

    # Initialize extensions if the database is configured
    if app.config["DB_CONFIGURED"]:
        db.init_app(app)

        # Create all tables
        with app.app_context():
            db.create_all()

            login_manager.init_app(app)
            login_manager.login_view = "auth.login"

            def get_user_by_id(user_id):
                from openwebpos.blueprints.user.models.UserModel import User

                return User.query.get(user_id)
