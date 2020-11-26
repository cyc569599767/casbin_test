# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask import request
from flask_login import current_user
from casbin_test import enforcer


def check_permission(func):
    """
    装饰器,验证请求权限
    """

    def wrapper(*args, **kwargs):
        sub = current_user.username  # 已登录用户的用户名
        dom = request.form.get('user_domain')  # 用户所属域
        resource_domain = request.form.get("resource_domain") if request.form.get("resource_domain") else "default"

        obj = {
            'url': request.path,  # 资源
            'dom': resource_domain  # 资源所属域
        }
        act = request.method  # 操作方法

        if not dom:
            dom = ''
        # 验证权限

        result = enforcer.enforce(sub, dom, obj, act)
        print(f" [sub: {sub}]---[dom: {dom}]---[obj: {obj}]---[act: {act}]---[验证结果: {result}]")

        if result:  # 验证通过
            return func(*args, **kwargs)
        else:
            return "无权限访问"

    return wrapper
