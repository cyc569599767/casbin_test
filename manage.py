from flask_restful import abort
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from casbin_test import create_app
from casbin_test import db
from casbin_test import casbin_auth

app = create_app()
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.before_request
def check_permission():
    subs = ["bob", "zeta"]
    objs = ["data1", "data2"]
    acts = ["read", "write"]


@app.errorhandler(403)
def err_403(arg):
    return "无权限访问"


if __name__ == '__main__':
    manager.run()
