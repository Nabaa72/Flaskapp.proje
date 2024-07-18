#from . import app
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_modals import Modal
from flask_mail import Mail
from pythonic.config import Config

app = Flask(__name__)


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate(db)
ckeditor = CKEditor()
modal = Modal()
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"
mail = Mail()


def create_app():
    app.config.from_object(Config)
    print(app.config)
    db.init_app(app)

    with app.app_context():
        print("Creating tables.")
        db.create_all()

    bcrypt.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)
    modal.init_app(app)
    mail.init_app(app)

    from pythonic.main.routes import main
    from pythonic.users.routes import users
    from pythonic.lessons.routes import lessons
    from pythonic.courses.routes import courses_bp


    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(lessons)
    app.register_blueprint(courses_bp)

    return app