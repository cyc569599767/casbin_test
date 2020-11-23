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
        obj = request.path # 访问的资源
        dom = request.args.get('domain') # 资源所属域
        act = request.method # 请求方法, GET 或者 post中的 method 属性值

        if not dom:
            dom = 'default'
        # 验证权限
        result = enforcer.enforce(sub, obj, dom, act)
        print(f" [sub: {sub}]---[obj: {obj}]---[dom: {dom}]---[act: {act}]---[验证结果: {result}]")

        if result:  # 验证通过
            return func(*args, **kwargs)
        else:
            return "无权限访问"

    return wrapper
