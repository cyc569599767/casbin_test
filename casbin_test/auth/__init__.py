# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask import Blueprint
from flask_restful import Api
from .views import Authorities


# 创建蓝图对象,管理资源
auth_bp = Blueprint('auth', __name__)
# 蓝图遵循 restful 风格
auth_api = Api(auth_bp)

# 配置路由和接口类的对应关系
auth_api.add_resource(Authorities, "/authorities")
