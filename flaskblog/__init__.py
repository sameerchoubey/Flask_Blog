from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' 
login_manager.login_message_category = 'info' 

mail = Mail()


# mail_settings = {
#     "MAIL_SERVER":'smtp.gmail.com',
#     "MAIL_PORT":465,
#     "MAIL_USE_TLS":False,
#     "MAIL_USE_SSL":True,
#     "MAIL_USERNAME":os.environ.get['EMAIL_USER'],
#     "MAIL_PASSWORD":os.environ.get['EMAIL_PASSWORD']
# }
# app.config.update(mail_settings)
# mail = Mail(app)

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

