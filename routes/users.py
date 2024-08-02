import sqlite3
from flask import Blueprint, jsonify, request, make_response

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/register', methods=["GET"])
def register():
    username = request.args.get("username")
    passwd = request.args.get("password")

    con = sqlite3.connect("database.db")

    cur = con.cursor()
    cur.execute("insert into users (username, password) values ('%s', '%s')" % (username, passwd))

    data = cur.fetchone()
    if data:
        return jsonify(data="Login successful"), 200
    else:
        return jsonify(data="Login unsuccessful"), 403


@users_blueprint.route('/login', methods=["GET"])
def login():
    username = request.args.get("username")
    passwd = request.args.get("password")

    con = sqlite3.connect("database.db")

    cur = con.cursor()
    cur.execute("select * from users where username = '%s' and password = '%s'" % (username, passwd))

    data = cur.fetchone()
    if data:
        return jsonify(data="Login successful"), 200
    else:
        return jsonify(data="Login unsuccessful"), 403


@users_blueprint.route('/get-user')
def get_user():
    x = request.args.get("x")
    return make_response("found {}".format(x))