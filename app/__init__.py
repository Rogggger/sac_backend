from flask import Flask
from app.libs.login import login_manager
from app.libs.db import db
from app.view.login import bp_login
from app.view.admin.arrange import bp_admin_arrange
from app.view.admin.info import bp_admin_info
from app.view.admin.rest import bp_admin_rest
from app.view.user.rest import bp_rest
from app.view.user.info import bp_info
from app.view.user.schedule import bp_schedule


def create_app(object_name):
    app = Flask(__name__)
    app.config.from_object(object_name)

    app.register_blueprint(bp_admin_arrange)
    app.register_blueprint(bp_admin_info)
    app.register_blueprint(bp_admin_rest)
    app.register_blueprint(bp_login)
    app.register_blueprint(bp_rest)
    app.register_blueprint(bp_info)
    app.register_blueprint(bp_schedule)

    login_manager.init_app(app)
    db.init_app(app)

    return app
