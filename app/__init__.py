from flask import Flask
from app.libs.login import login_manager
from app.libs.db import db
from app.view.admin import bp_admin
from app.view.login import bp_login
from app.view.user import bp_user


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    app.register_blueprint(bp_admin)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_user)

    login_manager.init_app(app)
    db.init_app(app)

    return app
