from pyfcm import FCMNotification


def send_notification(message_title,message_body,registration_id):
    push_service = FCMNotification(api_key="AAAAR7e9Yto:APA91bFqvc6jMbYxYBgi0MhIpRU7PGJT_OrZiKovULXJSm3tvYFt6R41XrTyikJenL0xw0HoFEzlC8KeqV4oULTpHPQSUmE49pjVCKyhKptvf3rHKPmXzk_s-wcOqAskzohic2y-3HxF")
    result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
# OR initialize with proxies

#proxy_dict = {
#          "http"  : "http://127.0.0.1",
#          "https" : "http://127.0.0.1",
#        }
#push_service = FCMNotification(api_key="<api-key>", proxy_dict=proxy_dict)

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

#registration_id = "e1b4irQoyJ8:APA91bHP_1Xya_q7GfMNTrpGusIqkynL3Jyn_aALYG3z6MmXG5unqSuZCSidVd82BEVvQdfTUV3g2b_ug5leqlVvmWrrPYh4jwqvh2qvS2MHQG3PJZMJptWwOFuj5vrdT-N7XqFgnn9z"
#message_title = "Uber update"
#message_body = "Hi john, your customized news for today is ready"
#send_notification("hello","Helloworld",registration_id)

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