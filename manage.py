from flask_script import Manager, Server
from app import create_app
from app.libs.db import db
from app.model.user import User
from app.model.schedule import Schedule
from app.model.position import Position
from app.model.info import Info
from app.model.department import Department
from app.model.rest import Rest
import config

app = create_app(config)
manager = Manager(app)


@manager.command
def createdb():
    with app.app_context():
        db.drop_all()
        db.create_all()


manager.add_command('runserver', Server(
    use_reloader=True,
    host='0.0.0.0',
    port=5000
    )
)

if __name__ == '__main__':
    manager.run()
