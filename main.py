from flask import Flask
from routes.main import main_blueprint
from routes.get_user_uploaded_memes import get_user_uploaded_memes_blueprint
from routes.users import users_blueprint


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(get_user_uploaded_memes_blueprint)
app.register_blueprint(users_blueprint)


if __name__ == "__main__":
    print("Starting app....")
    app.run(host="0.0.0.0", port=8081, debug=True)
