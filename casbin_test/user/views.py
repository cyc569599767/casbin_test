# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask_restful import Resource, reqparse
from models import Users, Domains, Roles
from casbin_test import db
from casbin_test import casbin_auth


class User(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int)
        self.parser.add_argument('username', type=str)
        self.parser.add_argument('role_id', type=int)
        self.parser.add_argument('domain_id', type=int)
        self.parser.add_argument('email', type=str, default="aaa@11.com")

        self.args = self.parser.parse_args()

        self.id = self.args.get('id')
        self.username = self.args.get('username')
        self.email = self.args.get('email')
        self.role_id = self.args.get('role_id')
        self.domain_id = self.args.get('domain_id')
        self.result = {
            'status': "success",
            'msg': "操作成功",
            "code": 200
        }

    def get(self):
        """
        查询用户信息
        :return:
        """
        user_obj = Users.query.filter_by(id=self.id).first()
        user_role_domain_list = []
        if not user_obj:
            self.result = {
                'status': "error",
                'msg': f"查询失败,用户id: {self.id} 不存在",
                "code": 200
            }
            return self.result

        domain_objs = Domains.query.all()

        for domain in domain_objs:
            print(f"{user_obj.username} , {domain.domain_name}")
            res = casbin_auth.enforcer.get_roles_for_user_in_domain(user_obj.username, domain.domain_name)
            print(f"res: {res}")
            if res:
                user_role_domain_list.append(res)

        print(f"user_role_domain_list: {user_role_domain_list}")

        self.result['result'] = {
            "id": user_obj.id,
            "user_name": user_obj.username,
            "email": user_obj.email,
            "result": user_role_domain_list
        }

        return self.result

    def post(self):
        """
        新增用户
        :return:
        """
        try:
            user = Users(username=self.username, email=self.email)
            db.session.add(user)
            db.session.commit()

        except:
            self.result = {
                'status': "error",
                'msg': f"创建失败,用户名或邮箱已被注册使用.",
                "code": 200
            }

        role_obj = Roles.query.filter_by(id=self.role_id).first()
        domain_obj = Domains.query.filter_by(id=self.domain_id).first()

        casbin_auth.enforcer.add_role_for_user_in_domain(self.username, role_obj.role_name, domain_obj.domain_name)

        return self.result
