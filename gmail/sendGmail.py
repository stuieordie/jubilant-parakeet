#! /usr/bin/python3

import smtplib

gmail_user = 'email_addr'
gmail_password = 'email_pass'

mail_to = "to_addr"
mail_from = "from_addr"

def sendDisconnect():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    DisconnectMessageBody = "To: "+mail_to+"\n"
    DisconnectMessageBody += "From: "+mail_from+"\n"
    DisconnectMessageBody += "Subject: Galaxy-S10 Disconnected from Home Wifi\n\n" 
    DisconnectMessageBody += "Your Galaxy-S10 has disconnected from your home Wifi and the Blink system has been armed\n"
    server.sendmail(sendFrom, sendTo, DisconnectMessageBody)
   
def sendConnect():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    ConnectMessageBody = "To: "+mail_to+"\n"
    ConnectMessageBody += "From: "+mail_from+"\n"
    ConnectMessageBody += "Subject: Galaxy-S10 Connected to Home Wifi\n\n" 
    ConnectMessageBody += "Your Galaxy-S10 has connected to your home Wifi and the Blink system has been disarmed\n"
    server.sendmail(sendFrom, sendTo, ConnectMessageBody)
