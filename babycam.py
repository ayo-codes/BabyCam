import BlynkLib # imports the blynk library which helps us connect to the mobile app
from sense_hat import SenseHat # imports the library to enable use sensehat features
from time import sleep #imports time functions
from dotenv import dotenv_values #imports .env values 
import RPi.GPIO as GPIO #allows us to use the GPIO pins
from w1thermsensor import W1ThermSensor #allows us to use the Ds18b20 temperature sensor

#loads MQTT configuration values from .env file
config = dotenv_values(".env")

#initialise Blynk , Put in your own keys into blynk_auth in .env 
blynk = BlynkLib.Blynk(config['BLYNK_AUTH'])

#initialise SenseHAT 
sense = SenseHat()
sense.clear()

#motion sensor 
motionPin = 21 #GPIO pin 21 
GPIO.setmode(GPIO.BCM) # sets the GPIO to BCM numbering system 
GPIO.setup(motionPin,GPIO.IN) # sets GPIO 21 as the input pin 

#initialise the ds18b20 temp sensor
sensor = W1ThermSensor()

#Runs the connection between blynk and raspberry pi 
try:
  while True:
    blynk.run()
    blynk.virtual_write(4,round(sense.humidity,2)) #writes to virtual pin 4 and sends data from the senseHAT for humidity
    motion = GPIO.input(motionPin) # set the variable motion as the input of the motionPin 
    blynk.virtual_write(5,motion) # writes to virtual pin 5 and data sent is the value of the variable motion
    temperatureDs18b20 = sensor.get_temperature()
    blynk.virtual_write(6,temperatureDs18b20)
    sleep(.5)
except KeyboardInterrupt:
  GPIO.cleanup()
  print('GPIO Good to Go')