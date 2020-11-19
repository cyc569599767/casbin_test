# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask_restful import Resource, reqparse
from casbin_test import casbin_auth
from models import Users, Roles, Domains, Resources, Operations


class Authorities(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("user_id", type=int)
        self.parser.add_argument("username", type=str)
        self.parser.add_argument("user_domain", type=str)
        self.parser.add_argument("resource", type=str)
        self.parser.add_argument("operation", type=str)

        self.result = {
            'status': "success",
            'msg': "操作成功",
            "code": 200
        }

    def get(self):
        """
        群查
        :return:
        """
        user_objs = Users.query.all()
        role_objs = Roles.query.all()
        domain_objs = Domains.query.all()
        resource_objs = Resources.query.all()
        operation_objs = Operations.query.all()

        user_role_list = []

        # 用户管理列表
        for user in user_objs:
            user_role_list.append(casbin_auth.enforcer.get_roles_for_user(user.username))
        print(user_role_list)

        return 'ok'
