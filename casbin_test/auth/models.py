# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from .. import db


class Permission(db.Model):
    """
    casbin 权限
    """
    __tablename__ = "permissions"
    id = db.Column(db.Integer, primary_key=True)
    ptype = db.Column(db.String(255))
    v0 = db.Column(db.String(255))
    v1 = db.Column(db.String(255))
    v2 = db.Column(db.String(255))
    v3 = db.Column(db.String(255))
    v4 = db.Column(db.String(255))
    v5 = db.Column(db.String(255))
