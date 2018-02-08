#!/usr/bin/env python
from flask_script import Manager
from app import *
from app.model import User

app = create_app()
manager = Manager(app)

@manager.command
def adduser(email, username, admin=True):
    """Register a new user."""
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: passwords do not match.')
    database.create_all()
    user = User(email=email, username=username,password = password,admin = admin)
    database.session.add(user)
    database.session.commit()
    print('User {0} was registered successfully.'.format(username))

if __name__ == '__main__':
    manager.run()
