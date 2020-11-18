# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from  .casbin_adapter import CasbinAdapter
import os
import casbin


class Auth:
    def __init__(self):
        self.enforcer = None

    def init_auth(self,app):
        adapter = CasbinAdapter(app)
        enforcer = casbin.Enforcer("policy.conf",adapter)
        self.enforcer = enforcer
