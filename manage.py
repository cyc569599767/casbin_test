from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from casbin_test import create_app, db, enforcer

app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)

# todo: 自定义403界面


if __name__ == '__main__':
    manager.run()
