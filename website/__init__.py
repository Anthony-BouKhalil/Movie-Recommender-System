from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from pathlib import Path
from dotenv import load_dotenv
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    # Load the Token from .env file
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    key = os.environ['KEY']

    # Encrypt session data 
    app.config['SECRET_KEY'] = key
    # Store the database in the website folder
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    create_db(app)

    login_manager = LoginManager()
    # Flask will redirect to the login page if the user is not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Check if a user id is stored in the session
        return User.query.get(int(user_id))

    return app

def create_db(app):
    if not os.path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Database created!")