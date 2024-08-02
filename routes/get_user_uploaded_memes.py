import pickle
from base64 import b64encode, b64decode
from uuid import uuid1

from flask import Blueprint, render_template_string, request, make_response
import logging

get_user_uploaded_memes_blueprint = Blueprint('hello', __name__)


class UserID:
    def __init__(self, uuid=None):
        self.uuid = str(uuid1())

    def __str__(self):
        return self.uuid


@get_user_uploaded_memes_blueprint.route("/get-user-uploaded-memes")
def get_user_uploaded_memes():
    user_obj = request.cookies.get('uuid')
    if user_obj is None:

        msg = "Seems like you didn't have a cookie. No worries! I'll set one now!"
        response = make_response(msg)
        user_obj = UserID()

        response.set_cookie('uuid', b64encode(pickle.dumps(user_obj)))
        return response
    else:
        return "Hey there! {}!".format(pickle.loads(b64decode(user_obj)))
