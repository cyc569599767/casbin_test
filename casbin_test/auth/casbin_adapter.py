# _*_ coding: utf-8 _*_
__author__ = 'yaco'

"""
适配器,casbin 策略存储在 mysql 数据库中
"""

from casbin import persist
from .. import db
from .models import Permission


class CasbinAdapter(persist.Adapter):
    """
    the interface for Casbin adapters
    """
    def __init__(self,app):
        self.app = app

    def load_policy(self, model):
        """
        loads all policy rules from the storage
        :param model:
        :return:
        """
        with self.app.app_context():
            lines = Permission.query.all()
            for line in lines:
                persist.load_policy_line(str(line), model)

    def _save_policy_line(self,ptype,rule):
        with self.app.app_context():
            line = Permission(ptype=ptype)
            for i, v in enumerate(rule):
                setattr(line, 'v{}'.format(i), v)
            db.session.add(line)
            db.session.commit()

    def save_policy(self, model):
        """
        saves all policy rules to the storage
        :param model:
        :return:
        """
        with self.app.app_context():
            for sec in ['p','g','g2']:
                if sec not in model.model.keys():
                    continue
                for ptype, ast in model.model[sec].items():
                    for rule in ast.policy:
                        self._save_policy_line(ptype,rule)
        return True

    def add_policy(self,sec,ptype,rule):
        """
        add a policy rule to the storage
        :param sec:
        :param ptype:
        :param rule:
        :return:
        """
        self._save_policy_line(ptype, rule)

    def remove_policy(self, sec, ptype, rule):
        """
        remove a policy rule from the storage
        :param sec:
        :param ptype:
        :param rule:
        :return:
        """
        with self.app.app_context():
            query = Permission.query.filter(Permission.ptype==ptype)
            for i, v in enumerate(rule):
                query = query.filter(getattr(Permission, 'v{}'.format(i)) == v)
            r = query.delete()
            db.session.commit()

        return True if r>0 else False

    def remove_filtered_policy(self, sec, ptype, field_index, *field_values):
        """
        removes policy rules that match the filter from the storage
        this is part of the Auto-Save feature
        :param sec:
        :param ptype:
        :param field_index:
        :param field_values:
        :return:
        """
        with self.app.app_context():
            query = Permission.query.filter(Permission.ptype==ptype)
            if not (0<=field_index<=5):
                return False
            if not (1<=field_index+len(field_values)<=6):
                return False
            for i,v in enumerate(field_values):
                query = query.filter(getattr(Permission, 'v{}'.format(field_index + i)) ==v)
            r = query.delete()
            db.session.commit()

        return True if r>0 else False

    def __del__(self):
        with self.app.app_context():
            db.session.close(0)