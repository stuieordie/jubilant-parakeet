#! /usr/bin/python3

import requests, json

wirepusher_id = "get_your_own_id"

def sendPushArmed():
    url = "https://wirepusher.com/send"
    querystring = {"id":wirepusher_id,"title":"Blink Armed","message":"Galaxy-S10 disconnected, Blink is armed","type":"Blink"}
    payload = ""
    response = requests.request("POST", url, data=payload, params=querystring)

def sendPushDisarmed():
    url = "https://wirepusher.com/send"
    querystring = {"id":wirepusher_id,"title":"Blink Disarmed","message":"Galaxy-S10 connected, Blink is disarmed","type":"Blink"}
    payload = ""
    response = requests.request("POST", url, data=payload, params=querystring)
