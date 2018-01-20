from .import database
from werkzeug.security import generate_password_hash, check_password_hash


class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    email = database.Column(database.String(64),nullable=False, unique=True, index=True)
    username = database.Column(database.String(64),nullable=False, unique=True, index=True)
    password_hash = database.Column(database.String(128))


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

    

