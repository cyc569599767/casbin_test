from casbin_test import create_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from casbin_test import db

'''

def init_auth():
    from app.auth import Auth
    casbin_auth = Auth()
    return casbin_auth
    
casbin_auth = init_auth()

@app.befor_request
def check_permission():
    dom = request.args.get('dom')
    if not dom:
        dom = 'domain::default'
    try:
        sub = casbin_auth.enforcer.get_roles_for_user_in_domain(current_user.username,dom)[0]
    except:
        sub = 'role::vistor;
        
    obj = request.path
    act = request.method
    res = casbin_auth.enforcer.enforce(sub,dom,obj,act)
    
    if not res:
        abort(403)
    
@app.errorhandler(403):
def err_403(arg):
    return "无权限访问"
'''


app = create_app()
manager=Manager(app)
Migrate(app,db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
