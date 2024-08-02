from flask import Blueprint, request, render_template_string
from flask import Flask, request, render_template
from flask_mail import Mail, Message

reset_password_blueprint = Blueprint('hello', __name__)

mail = Mail(app)


@reset_password_blueprint.route("/reset_password")
def reset_password():
    email = request.form.get("email")
    if not email:
        return "Invalid email", 400

    reset_link = "https://"+request.host+"reset/"+request.headers.get('reset_token')
    msg = Message('Password reset request', recipients=[email])
    msg.body = "Please click on the link to reset your password: " + reset_link

    mail.send(msg)
    return "Password reset email sent!"
