import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_googlemaps import GoogleMaps


bootstrap = Bootstrap()
database = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:enazumaeleven@localhost/safedrive'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or '3cjdaj#dsalp'
    app.config['INCIDENTS_PER_PAGE']= 10
    app.config['GOOGLEMAPS_KEY'] = "AIzaSyDxrZwnqA7Tm9uLeguM8XK78GqB-ZHIbJE"
    GoogleMaps(app)
    bootstrap.init_app(app)
    database.init_app(app)
    login_manager.init_app(app)
    moment = Moment(app)
    

    from authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint)

    from safedrive import safedrive as safedrive_blueprint
    app.register_blueprint(safedrive_blueprint)
    
    return app
