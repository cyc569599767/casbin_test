# _*_ coding: utf-8 _*_
__author__ = 'yaco'

from flask import render_template
from flask import Blueprint

test01 = Blueprint('test01', __name__)


@test01.route("/", methods=['GET'])
def index():
    return render_template('index.html')
