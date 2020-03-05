# Blink Arm/Disarm Based on Wifi Status
The code in this repository would run on my computer on my home network on a 1 minute interval. If my Samsung phone connected to the Wifi in the house, it would disarm the blink camera system. If I left the house and the phone disconnected from the Wifi, it would arm. I used this a method of geo-fencing because I found the IFTTT to be unreliable. Some fun stuff I added is on arm/disarm I had the computer play some .wav files. I've since stopped using this and gone back to IFTTT

### Goal Of Blink Scripting
- Arm the blink system when I'm not home and disarm when I am
- Arm the blink system at 00:00 regardless of whose home and disarm at 06:00
- Remember to disable cron from daily arms/disarms when on vacation
- Use the pynetgear libraries to check for devices connected to wifi (Samsung S10)
- Download the motion clips for archive
