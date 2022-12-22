import BlynkLib # imports the blynk library which helps us connect to the mobile app
from sense_hat import SenseHat # imports the library to enable use sensehat features
from time import sleep #imports time functions
from dotenv import dotenv_values #imports .env values 

#loads MQTT configuration values from .env file
config = dotenv_values(".env")

#initialise Blynk , Put in your own keys into blynk_auth in .env 
blynk = BlynkLib.Blynk(config['BLYNK_AUTH'])

#initialise SenseHAT 
sense = SenseHat()
sense.clear()

#Runs the connection between blynk and raspberry pi 
while True:
  blynk.run()
  blynk.virtual_write(4,round(sense.humidity,2)) #writes to virtual pin 4 and sends data from the senseHAT for humidity
  sleep(.5)
