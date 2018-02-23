from flask import render_template, flash, redirect, url_for, abort,\
    request, current_app
from flask_login import login_required, current_user
from .. import database
from ..model import User,Incidents
from . import safedrive
from .form import ProfileForm
import urllib2
import cookielib

TestUser = "None"

def sms(message,number):   
    username = "9591254802"
    passwd = "enazumaeleven"

    message = "+".join(message.split(' '))

 #logging into the sms site
    url ='http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'

 #For cookies

    cj= cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

 #Adding header details
    opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
    try:
        usock =opener.open(url, data)
    except IOError:
        print "error"
        #return()

    jession_id =str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
    try:
        sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
        print "error"
        #return()

    print "success"








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
        incident = Incidents(test_Score = result,user_id = user.id)
        database.session.add(incident)
        database.session.commit()
        msg = user.name + " is not in a condition to drive please pick him up"
        sms(msg,user.emergency_no)
        return render_template('test/fail.html')