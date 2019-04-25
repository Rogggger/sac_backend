from flask_script import Manager, Server
from app import create_app
from app.libs.db import db
from app.model import *
import config

app = create_app(config)
manager = Manager(app)


@manager.command
def createdb():
    with app.app_context():
        db.drop_all()
        db.create_all()

@manager.shell
def make_shell_context():
    return dict(app=app, db=db)

manager.add_command('runserver', Server(
    use_reloader=True,
    host='0.0.0.0',
    port=5000)
)

if __name__ == '__main__':
    manager.run()
