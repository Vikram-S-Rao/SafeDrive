from datetime import datetime
import calendar
import hashlib
from .import database,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import request, current_app


class User(UserMixin,database.Model):
    __tablename__ = 'User'
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(64),nullable=False, unique=True, index=True)
    username = database.Column(database.String(64),nullable=False, unique=True, index=True)
    name = database.Column(database.String(64))
    password_hash = database.Column(database.String(128))
    device_id = database.Column(database.String(16))
    vehicle_no = database.Column(database.String(15))
    age = database.Column(database.Integer)
    gender = database.Column(database.String(10))
    phone_no = database.Column(database.String(10))
    emergency_no = database.Column(database.String(10))
    address = database.Column(database.String(128))
    admin = database.Column(database.Boolean) 
    avatar_hash = database.Column(database.String(32))
    token = database.Column(database.String(1024))
    incidents = database.relationship('Incidents', lazy='dynamic', backref='user')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.email is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(
                self.email.encode('utf-8')).hexdigest()


    def __repr__(self):
        return '<User %r>' % self.username
    
    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def gravatar(self, size=100, default='identicon', rating='g'):
        if request.is_secure:
            url = 'https://secure.gravatar.com/avatar'
        else:
            url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or \
               hashlib.md5(self.email.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

    
class Incidents(database.Model):
    __tablename__='Incidents'
    id=database.Column(database.Integer,primary_key=True)
    location_lat = database.Column(database.String(10))
    location_long = database.Column(database.String(10))
    date=database.Column(database.DateTime(),default=datetime.now)
    day = database.Column(database.String(10))
    time = database.Column(database.Integer)
    test_Score = database.Column(database.Integer)
    bac = database.Column(database.Integer)
    country = database.Column(database.String(30))
    city = database.Column(database.String(30))
    locality = database.Column(database.String(1024))
    current_in = database.Column(database.Boolean)
    user_id = database.Column(database.Integer, database.ForeignKey('User.id'))
    
class Tracker(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(64),nullable=False, unique=True, index=True)
    username = database.Column(database.String(64),nullable=False, unique=True, index=True)
    password_hash = database.Column(database.String(128))
    tracker_id= database.Column(database.String(64),database.ForeignKey('User.email'))
    token = database.Column(database.String(1024))


    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)
