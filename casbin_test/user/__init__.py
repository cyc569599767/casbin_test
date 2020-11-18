# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask import Blueprint
from flask_restful import Api

# 创建蓝图对象,管理资源
user_bp = Blueprint('user', __name__)
# 蓝图遵循 restful 风格
api = Api(user_bp)

from .views import User
api.add_resource(User, "/user")
