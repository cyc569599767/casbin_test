# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask_restful import Resource, reqparse
from casbin_test import enforcer
from models import Users, Roles, Domains, Resources, Operations
from utils.wrappers import check_permission


class Authorities(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("user_id", type=int)
        self.parser.add_argument("username", type=str)
        self.parser.add_argument("method", type=str)
        self.parser.add_argument("domain_name", type=str)
        self.parser.add_argument("role_name", type=str)
        self.parser.add_argument("resource_name", type=str)
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

        # 用户管理列表,展示用户-角色关系
        for user in user_objs:
            user_role_list.append({
                user.username: enforcer.get_roles_for_user(user.username)
            })

        return user_role_list

    # @check_permission
    def post(self):
        """
        权限管理, 负责新增/删除/修改
        :return:
        """
        args = self.parser.parse_args()
        method = args.get('method')

        if method == "addUserRoleInDomain":
            # 授予 用户username 在 域domain_name 内具有 role_name角色
            username = args.get("username")
            domain_name = args.get("domain_name")
            role_name = args.get("role_name")
            if username and domain_name and role_name:
                res = enforcer.add_role_for_user_in_domain(username, role_name, domain_name)
                if res:
                    enforcer.save_policy()  # 执行持久化
                else:
                    self.result['status'] = "fail"
                    self.result['msg'] = "重复授权"

        elif method == "addResourceInDomain":
            # 资源属于某个域
            domain_name = args.get("domain_name")
            resource_name = args.get("resource_name")
            if domain_name and resource_name:
                obj = Resources.query.filter_by(resource_name=resource_name).first()
                res = enforcer.add_named_grouping_policy('g2', obj.url, domain_name)
                if res:
                    enforcer.save_policy()  # 执行持久化
                else:
                    self.result['status'] = "fail"
                    self.result['msg'] = "重复授权"

        elif method == "update":
            pass
        else:
            pass

        return self.result
