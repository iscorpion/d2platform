from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from ddtrace import patch_all
from sqlalchemy import create_engine

db = SQLAlchemy()
engine = None

# patch_all()


def create_app():
    print("FUck this shit")
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from app.routes import routes
        # db.drop_all()
        db.create_all()
        engine = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"))

        return app
