from flask import Flask
from app.libs.login import login_manager
from app.libs.db import db
from app.view.user.account import bp_account


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    app.register_blueprint(bp_account)

    login_manager.init_app(app)
    db.init_app(app)

    return app
