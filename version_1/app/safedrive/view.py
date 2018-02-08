from flask import render_template, flash, redirect, url_for, abort,\
    request, current_app
from flask_login import login_required, current_user
from .. import database
from ..model import User
from . import safedrive
from .form import ProfileForm

TestUser = "None"
@safedrive.route('/')
def index():
    return render_template('safedrive/index.html')

@safedrive.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('safedrive/user.html', user=user)

@safedrive.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.device_id = form.device.data
        current_user.phone_no = form.phone.data
        current_user.address=form.address.data
        current_user.emergency_no=form.emergency.data
        database.session.add(current_user._get_current_object())
        database.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('safedrive.user', username=current_user.username))
    form.name.data = current_user.name
    form.device.data = current_user.device_id
    form.phone.data = current_user.phone_no
    form.address.data=current_user.address
    form.emergency.data=current_user.emergency_no
    return render_template('safedrive/profile.html', form=form)


@safedrive.route('/user/<username>/test')
def test(username):
    user = User.query.filter_by(username=username).first_or_404()
    TestUser = user
    return render_template('test/test.html')

@safedrive.route('/user/<username>/test/<result>')
def result(username,result):
    user = User.query.filter_by(username=username).first_or_404()
    if(int(result) >= 2):
        return render_template('test/result.html')
    else:
        return render_template('test/fail.html')