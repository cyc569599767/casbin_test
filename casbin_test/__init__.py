# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import casbin
import os
from flask_login import LoginManager

model_file_path = os.path.join(os.getcwd(), 'casbin_test', 'auth', 'casbinmodel.conf')
policy_file_path = os.path.join(os.getcwd(), 'casbin_test', 'auth', 'policy.csv')
enforcer = casbin.Enforcer(model_file_path, policy_file_path)

import simpleeval


def new_eval(*args):
    a = simpleeval.SimpleEval()
    expr = args[0]

    return a.eval(*args)


enforcer.add_function('eval', new_eval)

db = SQLAlchemy()

# 必须写在这里,在 db 下方,否则引起循环导入
from models import *
from .test01 import test01
from .user import user_bp
from .auth import auth_bp

# 登录认证
login_manager = LoginManager()
login_manager.login_message = u"对不起,您还没有登录"
login_manager.login_message_category = "info"
login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


def create_app():
    # 如果出现 TemplateNotFound的问题 ,需要在创建 Flask 对象的时候,指定 template_folder.
    # 一个项目只能有一个 Flask 对象,当 Flask 对象和 templates 文件夹在同一目录下时,可以直接找到 templates 文件夹
    app = Flask(__name__, template_folder="../templates", static_folder="", static_url_path="")
    app.config.from_object('settings.DevelopmentConfig')

    # 将db注册到app中
    db.init_app(app)

    # 注册蓝图
    register_blueprint(app)

    # 登录认证
    login_manager.init_app(app)

    return app


def register_blueprint(app):
    """
        注册蓝图函数
    :param app:
    :return:
    """
    app.register_blueprint(user_bp)
    app.register_blueprint(test01)
    app.register_blueprint(auth_bp)
