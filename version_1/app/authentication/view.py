from flask import render_template,current_app,request,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required
from ..model import User
from . import authentication
from .form import LoginForm,SignupForm 
from ..import database

@authentication.route('/login',methods=['GET','POST'])
def login():
    Form = LoginForm()
    if Form.validate_on_submit():
        user = User.query.filter_by(email=Form.email.data).first()
        if user is None or not user.verify_password(Form.password.data):
           flash('Invalid E-mail or Password')
           return redirect(url_for('.login'))
        login_user(user,False)
        return redirect(request.args.get('next') or url_for('safedrive.index'))
    return render_template('authentication/login.html', form=Form)

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('safedrive.index'))


@authentication.route('/signup',methods=['GET','POST'])
def signup():
    Form = SignupForm()
    if Form.validate_on_submit():
        user = User(email=Form.email.data,username=Form.username.data,password=Form.password.data)
        database.session.add(user)
        database.session.commit()
        flash('Sign Up Successfull.You can now Login.')
        return redirect(url_for('.login'))
    return render_template('authentication/signup.html', form=Form)



@authentication.route('/register',methods=['GET','POST'])
def register():
    username = request.json['Username']
    email = request.json['Email']
    password = request.json['Password']
    phone = request.json['Phone']
    device = request.json['Device']
    address = request.json['Address']
    emergency = request.json['Emergency']
    user = User(email = email,username = username,password = password,device_id = device,phone_no = phone,address =address,emergency_no = email)
    database.session.add(user)
    database.session.commit()
    return 'ok'
@authentication.route('/login/<email>/<password>',methods=['GET','POST'])
def LoginUser(email,password):
    user = User.query.filter_by(email=email).first()
    if user is None or not user.verify_password(password):
        return "Fail"
    return "Success"