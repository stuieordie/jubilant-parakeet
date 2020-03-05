#! /usr/bin/python3

from pynetgear_enhanced import NetgearEnhanced

'''
See https://pypi.org/project/pynetgear-enhanced/
'''

'''
This function takes a mac address string in format of "XX:XX:XX:XX:XX:XX"
and returns true if that mac address is connected, false if it is not
'''

router_password = "your router password"

def isMacConnected(mac):
    mac = mac.lower()
    netgear = NetgearEnhanced(password=router_password)
    devs = netgear.get_attached_devices()
    devMacs = {}
    for dev in devs:
        devMacs[dev.mac.lower()] = dev.name

    if mac in devMacs:
        conStatus = True
    else:
        conStatus = False

    return conStatus
x = isMacConnected('asdbc')
print(x)
