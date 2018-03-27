from flask import render_template, flash, redirect, url_for, abort,\
    request, current_app
from flask_login import login_required, current_user
from .. import database
from ..model import User,Incidents,Tracker
from . import safedrive
from .form import ProfileForm
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.palettes import Spectral6
from datetime import datetime
import calendar
import time
from bokeh.models.sources import ColumnDataSource
from bokeh.models import (HoverTool, FactorRange, Plot, LinearAxis, Grid,
                          Range1d)
from notify import send_notification,sms
import urllib2
import cookielib
import collections

TestUser = "None"




@safedrive.route('/')
def index():
    return render_template('safedrive/index.html')

@safedrive.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    pagination = user.incidents.order_by(Incidents.date.desc()).paginate(page, per_page=current_app.config['INCIDENTS_PER_PAGE'],
        error_out=False)
    incident_list = pagination.items
    return render_template('safedrive/user.html', user=user,incidents=incident_list,pagination=pagination)

@safedrive.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.age = form.age.data
        current_user.gender = form.gender.data
        current_user.vehicle_no = form.vehicle_no.data
        current_user.device_id = form.device.data
        current_user.phone_no = form.phone.data
        current_user.address=form.address.data
        current_user.emergency_no=form.emergency.data
        database.session.add(current_user._get_current_object())
        database.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('safedrive.user', username=current_user.username))
    form.name.data = current_user.name
    form.age.data = current_user.age
    form.gender.data = current_user.gender
    form.vehicle_no.data = current_user.vehicle_no
    form.device.data = current_user.device_id
    form.phone.data = current_user.phone_no
    form.address.data=current_user.address
    form.emergency.data=current_user.emergency_no
    return render_template('safedrive/profile.html', form=form)

@safedrive.route('/user/incident/<id>')
@login_required
def incident(id):
    inc = Incidents.query.get_or_404(id)
    return render_template('safedrive/incident.html',incident=inc)

@safedrive.route('/admin/dashboard')
@login_required
def dashboard():
    inc = Incidents.query.order_by(Incidents.date.desc())
    users = User.query.order_by(User.username).all()
    return render_template('safedrive/Dashboard.html',incidents=inc,users=users)




@safedrive.route('/admin/analytics')
def analytics(): 
    source,time,count = time_plot()
    plot = figure(x_range=(0,24),y_range=(0,10) ,plot_height=450,plot_width=450, title="Time Plot",
           toolbar_location=None, tools="")
    plot.vbar(x='time', top='count', width=0.9, color='color', legend="time", source=source)
    plot.xgrid.grid_line_color = None
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"
    script1, div1 = components(plot)

    source,age,count = age_plot() 
    plot = figure(x_range=(0,99),y_range=(0,10) ,plot_height=450,plot_width=1800, title="Age Plot",
           toolbar_location=None, tools="")
    plot.vbar(x='age', top='count', width=1.2, color='color', legend="age", source=source)
    plot.xgrid.grid_line_color = None
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"
    script2,div2= components(plot)

    source,day,count = day_plot() 
    plot = figure(x_range=['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday','Sunday'],y_range=(0,10) ,plot_height=450,plot_width=450, title="Day of the Week Plot",
           toolbar_location=None, tools="")
    plot.vbar(x='day', top='count', width=0.9, color='color', legend="day", source=source)
    plot.xgrid.grid_line_color = None
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"
    script3,div3= components(plot)

    source,city,count = city_plot() 
    plot = figure(x_range=city,y_range=(0,10) ,plot_height=450,plot_width=450, title="City Plot",
           toolbar_location=None, tools="")
    plot.vbar(x='city', top='count', width=0.9, color='color', legend="city", source=source)
    plot.xgrid.grid_line_color = None
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"
    script4,div4= components(plot)

    source,loc,count = loc_plot() 
    plot = figure(x_range=loc,y_range=(0,10) ,plot_height=450,plot_width=450, title="locality Plot",
           toolbar_location=None, tools="")
    plot.vbar(x='loc', top='count', width=0.9, color='color', legend="loc", source=source)
    plot.xgrid.grid_line_color = None
    plot.legend.orientation = "horizontal"
    plot.legend.location = "top_center"
    script5,div5= components(plot)
    return render_template("safedrive/chart.html",the_div1=div1, the_script1=script1,the_div2=div2, the_script2=script2,the_div3=div3, the_script3=script3,the_div4=div4, the_script4=script4, the_div5=div5, the_script5=script5)
    
def time_plot():
    time=[]
    timelist=[]
    count=[]
    inc = Incidents.query.order_by(Incidents.id)
    for i in inc:
        time.append(i.time)
    keys=collections.Counter(time)
    for key in keys.keys():
        timelist.append(key)
        count.append(keys[key])
    source = ColumnDataSource(data=dict(time=timelist, count=count, color=Spectral6))
    return source,timelist,count

def age_plot():
    ulist=[]
    agelist=[]
    count=[]
    users = User.query.order_by(User.id)
    for user in users:
        ulist.append(user.age)
    keys=collections.Counter(ulist)
    for key in keys.keys():
        agelist.append(key)
        count.append(keys[key])
    source = ColumnDataSource(data=dict(age=agelist, count=count, color=Spectral6))
    return source,agelist,count

def day_plot():
    day=[]
    daylist=[]
    count=[]
    inc = Incidents.query.order_by(Incidents.id)
    for i in inc:
        day.append(i.day)
    keys=collections.Counter(day)
    for key in keys.keys():
        daylist.append(key)
        count.append(keys[key])
    source = ColumnDataSource(data=dict(day=daylist, count=count, color=Spectral6))
    return source,daylist,count

def city_plot():
    city=[]
    citylist=[]
    count = []
    inc = Incidents.query.order_by(Incidents.id)
    for i in inc:
        city.append(i.city)
    keys=collections.Counter(city)
    for key in keys.keys():
        citylist.append(key)
        count.append(keys[key])
    source = ColumnDataSource(data=dict(city=citylist, count=count, color=Spectral6))
    return source,citylist,count

def loc_plot():
    loc=[]
    loclist=[]
    count = []
    inc = Incidents.query.order_by(Incidents.id)
    for i in inc:
        loc.append(i.locality)
    keys=collections.Counter(loc)
    for key in keys.keys():
        loclist.append(key)
        count.append(keys[key])
    source = ColumnDataSource(data=dict(loc=loclist, count=count, color=Spectral6))
    return source,loclist,count

    



@safedrive.route('/user/testresult',methods=['GET','POST'])
def result():
    email = request.json['Email']
    score = request.json['Score']
    country = request.json['Country']
    city = request.json['City']
    locality = request.json['Locality']
    latitude = request.json['Latitude']
    longitude = request.json['Longitude']
    user = User.query.filter_by(email=email).first()
    day = calendar.day_name[datetime.today().weekday()]
    cur_time = time.strftime("%H")
    incident = Incidents(location_lat =latitude,location_long = longitude,country = country,city = city,locality=locality,day = day,time=cur_time, test_Score = score,user_id = user.id)
    database.session.add(incident)
    database.session.commit()
    tracker = Tracker.query.filter_by(tracker_id = email).first()
    reg_id = tracker.token
    msg_head = "SAFE DRIVE"
    msg_body = user.name + " is not in a condition to drive. Please pick him up."
    send_notification(msg_head,msg_body,reg_id)
    #msg = user.name + " is not in a condition to drive please pick him up"
    #sms(msg,user.emergency_no)
    return 'Success'
    
@safedrive.route('/user/token')
def Token():
    email = request.json['Email']
    token = request.json['Token']
    user = User.query.filter_by(email=email).first()
    user.token = token 
    database.session.commit()
    return "Success"

