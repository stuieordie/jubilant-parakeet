#! /usr/bin/python3

import requests, json

def blinkLogin(username, password):
    # Login to Blink servers
    url = "https://rest.prod.immedia-semi.com/login"
    data = {"password": password, "client_specifier": "iPhone 9.2 | 2.2 | 222", "email": username}
    payload = json.dumps(data)
    headers = {
        'content-type': "application/json",
        'host': "prod.immedia-semi.com"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        region = response.json()['region']
        region = list(region.keys())[0]
        network = response.json()['networks']
        network = list(network.keys())[0]
        authToken = response.json()["authtoken"]["authtoken"]
    else:
        region = False
        network = False
        authToken = False
    return region, network, authToken

def blinkArmSystem(region, network, authToken):
    url = "https://rest-"+region+".immedia-semi.com/network/"+network+"/arm"
    payload = ""
    headers = {
        'host': "prod.immedia-semi.com",
        'token_auth': authToken
        }
    response = requests.request("POST", url, data=payload, headers=headers)

def blinkDisarmSystem(region, network, authToken):
    url = "https://rest-"+region+".immedia-semi.com/network/"+network+"/disarm"
    payload = ""
    headers = {
        'host': "prod.immedia-semi.com",
        'token_auth': authToken
        }
    response = requests.request("POST", url, data=payload, headers=headers)
