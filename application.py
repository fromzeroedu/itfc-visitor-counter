from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# setup db
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    # initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    return app
