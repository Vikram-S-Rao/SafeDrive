from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
database = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:enazumaeleven@localhost/safedrive'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    bootstrap.init_app(app)
    database.init_app(app)

    from authentication import authentication as authentication_blueprint
    app.register_blueprint(authentication_blueprint)
    
    return app
