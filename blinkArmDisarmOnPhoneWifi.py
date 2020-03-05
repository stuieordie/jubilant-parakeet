#! /usr/bin/python3

'''
Summary

script runs, gets connection state  and compares to previous state (from file). If states
are the same, then exits. If not the same, then either arms or disarms the system. If arming
the system, 4 more attempts are made to see if the connection state is true before actually
arming. This prevents the system being armed for temporary disconnects such as walking outside

'''
import sys, datetime, requests, json, time
from playsound import playsound
sys.path.insert(0, '/home/mstuart/scripts/netgear')
sys.path.insert(0, '/home/mstuart/scripts/blink/')
sys.path.insert(0, '/home/mstuart/scripts/gmail/')
sys.path.insert(0, '/home/mstuart/scripts/WirePusher/')

import macfindfunction, blinkCommand, sendGmail, send_gs10_notification as gs10

# S10 mac = E8:E8:B7:79:6F:A5

blinkUsername = 'username'
blinkPassword = 'password'

f1 = open('/home/mstuart/scripts/blink/previous_state.txt', 'r+')
f2 = open('/home/mstuart/scripts/blink/connection_status.log', 'a')

# Get the previous connection status, set file position marker back to 0
previous_state = f1.read().splitlines()[0].strip()
f1.seek(0)

# Get the current connection status
isconnected = macfindfunction.isMacConnected("E8:E8:B7:79:6F:A5")
if isconnected == True:
    current_state = "True"
    print(current_state, file=f1)
elif isconnected == False:
    current_state = "False"
    print(current_state, file=f1)

if current_state == previous_state:
    #print(str(datetime.datetime.now())+' no device connection status change, quitting', file=f2)
    sys.exit(0)
elif current_state == "True":
    print(str(datetime.datetime.now())+' DEVICE HAS CONNECTED - DISARMING BLINK SYSTEM!', file=f2)
    region, network, authToken = blinkCommand.blinkLogin(blinkUsername, blinkPassword)
    time.sleep(.5)
    blinkCommand.blinkDisarmSystem(region, network, authToken)
    gs10.sendPushDisarmed()
    #sendGmail.sendConnect()
    #playsound('/home/mstuart/scripts/blink/blink_system_disarmed.wav')
elif current_state == "False":
    print(str(datetime.datetime.now())+' current state was False (device not found)', file=f2)
    x = 0
    while x < 5:
        print(str(datetime.datetime.now()), ' Re-checking for MAC address...', file=f2)
        isconnected = macfindfunction.isMacConnected("E8:E8:B7:79:6F:A5")
        if isconnected == True:
            print(str(datetime.datetime.now())+' MAC found on re-check, exiting', file=f2)
            current_state = "True"
            f1.seek(0)
            print(current_state, file=f1)
            sys.exit(0)
        x += 1
        time.sleep(4)
    print(str(datetime.datetime.now())+' DEVICE HAS DISCONNECTED - ARMING BLINK SYSTEM!', file=f2)
    region, network, authToken = blinkCommand.blinkLogin(blinkUsername, blinkPassword)
    time.sleep(.5)
    blinkCommand.blinkArmSystem(region, network, authToken)
    #sendGmail.sendDisconnect()
    gs10.sendPushArmed()
