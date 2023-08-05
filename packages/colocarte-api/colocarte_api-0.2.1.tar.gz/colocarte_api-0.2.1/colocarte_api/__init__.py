import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def configure_app(app):
    """Common configuration for development and production."""
    from . import bon_plan, coloc

    # blueprints
    app.register_blueprint(coloc.blueprint)
    app.register_blueprint(bon_plan.blueprint)

    # Database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)


def get_dev_app() -> Flask:
    """Create a development app, NOT SUITABLE FOR PRODUCTION."""

    app = Flask(__name__, static_url_path="", static_folder="../../frontend")
    app.config.update(
        TESTING=True, DEBUG=True, SQLALCHEMY_DATABASE_URI="sqlite:///../test.db"
    )

    configure_app(app)
    with app.app_context():
        db.create_all()

    return app


def get_prod_app() -> Flask:
    """Create a production ready app."""

    instance_path = os.environ.get("FLASK_INSTANCE_PATH")
    if instance_path is None:
        raise RuntimeError("Please set FLASK_INSTANCE_PATH (must be an absolute path).")

    app = Flask(
        __name__,
        instance_path=instance_path,
        instance_relative_config=True,
        static_folder=None,
    )
    app.config.update(
        SERVER_NAME="colocarte.wkerl.me",
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_SAMESITE="Lax",
    )
    app.config.from_pyfile("secrets.cfg")

    configure_app(app)
    return app
