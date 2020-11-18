# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .test01.models import *
from .user.models import *
from .test01 import test01
from .user import user_bp


def create_app():
    # 如果出现 TemplateNotFound的问题 ,需要在创建 Flask 对象的时候,指定 template_folder.
    # 一个项目只能有一个 Flask 对象,当 Flask 对象和 templates 文件夹在同一目录下时,可以直接找到 templates 文件夹
    app = Flask(__name__,template_folder="../templates",static_folder="",static_url_path="")
    app.config.from_object('settings.DevelopmentConfig')

    # 将db注册到app中
    db.init_app(app)

    # 注册蓝图
    register_blueprint(app)

    return app


def register_blueprint(app):
    """
        注册蓝图函数
    :param app:
    :return:
    """
    app.register_blueprint(user_bp)
    app.register_blueprint(test01)
