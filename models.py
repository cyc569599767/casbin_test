# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from casbin_test import db


class Users(db.Model):
    """
    用户表
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


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


class Domains(db.Model):
    """
    域名表
    """
    __tablename__ = 'domains'
    id = db.Column(db.Integer, primary_key=True)
    domain_name = db.Column(db.String(80), unique=True, nullable=False)


class Roles(db.Model):
    """
    角色表
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False)


class Resources(db.Model):
    """
    资源表
    """
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    resource_name = db.Column(db.String(80), unique=True, nullable=False)
    url = db.Column(db.String(80), unique=True, nullable=False)


class Operations(db.Model):
    """
    操作方法表
    """
    __tablename__ = 'operations'
    id = db.Column(db.Integer, primary_key=True)
    operation_name_cn = db.Column(db.String(80), unique=True, nullable=False)
    operation_name_en = db.Column(db.String(80), unique=True, nullable=False)
