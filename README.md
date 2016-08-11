# Python Garage Door
This is a VERY simple project for a standalone or network included garage door opener running on a Raspberry Pi. The Raspberry Pi is connected to a relay, which is then connected to the garage door opener wires. A webpage is served from the Pi with a button that activates the relay and raises, stops, or lowers the door. 

## Requirements
This project requires Python 2.7/3, as well as the time, RPi.GPIO, and web.py modules. Time and RPi.GPIO are typically already installed on newer versions of Raspian. 

## Notes
If you already have a home network, the Pi can be included in it, and the REST endpoint for the relay accessed that way. If, like us, your garage is separate from your home and is not reachable by an existing network, the Pi can host a wireless access point, which you can then connect to to use the opener. 
