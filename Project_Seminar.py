
#------------------------- Made By Rohit Kumar Sahu ----------------------#


import random
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from email import encoders
from datetime import datetime
import getpass
import sys
import numpy as np
import cv2
import time
import os
import zipfile
import cookielib
from stat import *
import urllib2



print('''
Password Generator
==================
''')


def sendsms():
    global c
    c = random.randint(1111,9999)
    message = "Your 4 Digit OTP is "+str(c) 
    number = "Your Phone Numeber"
 
    username = "Your Way2SMS username"
    passwd = "Your Way2SMS password"

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

    print "OTP Successfully Sent to the registered Mobile Number"
    #return ()


def Zip_Maker():

    
    zf = zipfile.ZipFile("Captured_Images.zip", "w")
    for dirname, subdirs, files in os.walk("Image_Captured"):
        zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
    zf.close()


def Face_Capture():
    #import the cascade for face detection
    face_cascade = cv2.CascadeClassifier('C:/opencv/build/etc/haarcascades/haarcascade_frontalface_alt.xml')
    # access the webcam (every webcam has a number, the default is 0)
    cap = cv2.VideoCapture(0)

    num = 0 
    while num<3:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # to detect faces in video
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        x = 0
        y = 20
        text_color = (0,255,0)

        cv2.imwrite('C:/Users/ACER/Desktop/Image_Captured/Face_Capture_'+str(num)+'.jpg',frame)
        num = num+1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()



def sendsms_Inform():
    message = "Someone Anonymously Tried To Access Your Account... Images of the unauthorized person is mailed to you" 
    number = "9830079457"
 
    username = "9830079457"
    passwd = "9830079457"

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

    print "Informed the Owner About Suspicious Activity"
    #return ()




def mailsend_Pics():
    fromaddr = 'Sender email address'
    passw='Sender Email Password'
    toaddr = 'Recipent Email ID'
    filename = "Passwords.txt"
    attachment = open("C:/Users/ACER/Desktop/Captured_Images.zip", "rb")
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Attention, Someone Accessed Your Account"
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="Captured_Images.zip"')
 
    msg.attach(part)
    body = "Below is the zip file which contains the images of the unauthorized Person"
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, passw)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print(" \n Mail Sent! to the Owner")
    server.quit()

 

def mailsend():
    fromaddr = "Sender email addres"
    passw="Sender Email Password"
    toaddr = r"Recipent Email ID"
    filename = "Passwords.txt"
    attachment = open("C:/Users/ACER/Desktop/Passwords.txt", "rb")
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Generated Passwords"
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="Passwords.txt"')
 
    msg.attach(part)
    body = "Below is the attachment which contain your Passwords"
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, passw)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print(" \n Mail Sent!")
    server.quit()
    
def pass_gen():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    smallletters = 'abcdefghijklmnopqrstuvwxyz'
    bigletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special = '!@£$%^&*().,?'
    mylist=[]
    number = raw_input('number of passwords?\n')
    if(number==''):
        print('No. of Passwords not entered\n')
        while(number==''):
            number=raw_input()
    number=int(number)
    global d
    length = raw_input('password length?\n')
    global user_username
    user_username = "Rohit"
    global user_passd
    user_passd="9804"
    if(length==''):
        print('Length of the password not entered...Please enter it\n')
        while(length==''):
            length=raw_input()
    length = int(length)
    if(length>=8):
        length=length-2
        first = raw_input('Enter the starting letter of your password\n')
        if(first==''):
            print("First Letter not entered....Please enter the first Letter.....\n")
            while(first==''):
                first=raw_input()
            
        if(first!='' and len(first)==1):
            print('''The Password Generated are
========================''')
            with open('C:/Users/ACER/Desktop/Passwords.txt','a') as the_file:
                the_file.write('Recorded at: %s\n' %datetime.now())
                the_file.write('=========================================\n')
            print("The Password are Generated..... To Access it Authenticate Your Details\n")
            for pwd in range(number):
                p=''
                for i in range(length):
                    while(len(p)<length):
                        p=p+random.choice(smallletters) + random.choice(bigletters) + random.choice(digits) + random.choice(special)
                        if(abs(len(p)-length-1)==1):
                            p=p+random.choice(special)
                        elif(abs(len(p)-length-1)==2):
                            p=p+random.choice(smallletters) + random.choice(digits)
                        elif(abs(len(p)-length-1)==3):
                            p=p+random.choice(bigletters) + random.choice(digits) + random.choice(smallletters)
                e=first+p
                mylist.append(e)
            print("Enter the username & password to get your passwords generated\n")
            username = raw_input('Enter the username\n')
            password = raw_input('Enter the password\n')
            if((username!= user_username and password!=user_passd) or (username==user_username and password!=user_passd) or (username!=user_username and password==user_passd)):
                print('The Credentials are Incorrect.....Please try again\n')
                count = int(5)
                print("Did You Forgot Your Password...Say Yes or No\n")
                forgot=raw_input()
                if(forgot=="Yes"):
                    sendsms()
                    f=1
                    otp=raw_input('Enter the 4 digit OTP sent to your phone\n')
                    otp=int(otp)
                    if(otp==int(c)):
                        print("OTP Matched\n")
                        new_pass=raw_input("Enter the new password\n")
                        print("Your New Password has been set\n")
                        username=raw_input("Enter Your Username\n")
                        password = raw_input("Enter Your Password\n")
                        if(username==user_username and password==new_pass):
                            with open('C:/Users/ACER/Desktop/Passwords.txt','a') as the_file:
                                for i in range(number):
                                    the_file.write(mylist[i]+'\n')
                            mailsend()
                        else:
                            print("The Credentials are not valid.....Please try again\n")
                    else:
                        print(c)
                        print("OTP did Not matched\n")
                    if(f!=1):
                        with open('C:/Users/ACER/Desktop/Passwords.txt','a') as the_file:
                            for i in range(number):
                                the_file.write(mylist[i]+'\n')
                        mailsend()
                elif(forgot=="No"):
                    while((username!=user_username and password!=user_passd) or (username==user_username and password!=user_passd) or (username!=user_username)):
                        if(count==0):
                            print("You do not have anymore attempts....You are not an authorized personnel\n")
                            Face_Capture()
                            Zip_Maker()
                            mailsend_Pics()
                            sendsms_Inform()
                            sys.exit()
                        else:
                            print('You have Total of '+str(count)+' attempts..\n')
                            username = raw_input('Enter the username\n')
                            password = raw_input('Enter the password\n')
                            count-=1
                    with open('C:/Users/ACER/Desktop/Passwords.txt','a') as the_file:
                        for i in range(number):
                            the_file.write(mylist[i]+'\n')
                    mailsend()
                else:
                    print("Enter Either Yes or No\n")
            elif(username==user_username and password==user_passd):
                with open('C:/Users/ACER/Desktop/Passwords.txt','a') as the_file:
                    for i in range(number):
                        the_file.write(mylist[i]+'\n')
                mailsend()
        else:
            print("The first character should have length 1\n")
        
    else:
        print("Insufficient Length for Strong Password\n")


if __name__ == "__main__":

  pass_gen()




















