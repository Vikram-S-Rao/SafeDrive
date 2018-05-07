from pyfcm import FCMNotification
import urllib2
import cookielib
import smtplib
from getpass import getpass
import sys
import os
from stat import *


def send_notification(message_title,message_body,registration_id):
    push_service = FCMNotification(api_key="AAAAR7e9Yto:APA91bFqvc6jMbYxYBgi0MhIpRU7PGJT_OrZiKovULXJSm3tvYFt6R41XrTyikJenL0xw0HoFEzlC8KeqV4oULTpHPQSUmE49pjVCKyhKptvf3rHKPmXzk_s-wcOqAskzohic2y-3HxF")
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)



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



def sendsms(message,number):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("vikram.nesamedtech@gmail.com", "enazumaeleven")
    s.sendmail("vikram.nesamedtech@gmail.com",number, message)
    s.quit()