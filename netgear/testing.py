#! /usr/bin/python3

import sys, time
import macfindfunction

x = 0
while x < 4:
    print(x, 'Seeing if MAC is connected...')
    isconnected = macfindfunction.isMacConnected("E8:E8:B7:79:6F:A5")
    if isconnected == True:
        print('MAC found, quitting')
        sys.exit(0)
    print(x, 'MAC not found')
    x += 1
    time.sleep(3)
print('Would arm the blink system...')
