import BlynkLib # imports the blynk library which helps us connect to the mobile app
from sense_hat import SenseHat # imports the library to enable use sensehat features
from time import sleep #imports time functions
from dotenv import dotenv_values #imports .env values 
import RPi.GPIO as GPIO #allows us to use the GPIO pins
from w1thermsensor import W1ThermSensor #allows us to use the Ds18b20 temperature sensor
import datetime
import smtplib # allows us to send emails
from email.mime.text import MIMEText #allows us to use text in the email
from email.mime.multipart import MIMEMultipart
from signal import pause
import logging # allows us to log events 

#loads MQTT configuration values from .env file
config = dotenv_values(".env")

#initialise Blynk , Put in your own keys into blynk_auth in .env 
blynk = BlynkLib.Blynk(config['BLYNK_AUTH'])

# configure logging
logging.basicConfig(level=logging.INFO)

#initialise SenseHAT 
sense = SenseHat()
sense.clear()

#motion sensor 
motionPin = 21 #GPIO pin 21 
GPIO.setmode(GPIO.BCM) # sets the GPIO to BCM numbering system 
GPIO.setup(motionPin,GPIO.IN) # sets GPIO 21 as the input pin 

#initialise the ds18b20 temp sensor
sensor = W1ThermSensor()

# send email define function 
def send_mail(eFrom, to, subject, text):
  # SMTP Server details: update to your credentials or use class server
  smtpServer = config['smtpServer'] #input smtp server address
  smtpUser = config['smtpUser'] #input smtp user name
  smtpPassword= config['smtpPassword'] #input your smtp password
  port= config['port'] # input your smtp port 

 # Construct MIME Multipart email message
  msg = MIMEMultipart()
  msg.attach(MIMEText(text))
  msg['Subject'] = subject

  # Authenticate with SMTP server and send
  s = smtplib.SMTP(smtpServer, port)
  s.login(smtpUser, smtpPassword)
  s.sendmail(eFrom, to, msg.as_string())
  s.quit()

#Runs the connection between blynk and raspberry pi and loop that waits for events to happen  
try:
  while True:
    blynk.run()
    blynk.virtual_write(4,round(sense.humidity,2)) #writes to virtual pin 4 and sends data from the senseHAT for humidity
    motion = GPIO.input(motionPin) # set the variable motion as the input of the motionPin 
    blynk.virtual_write(5,motion) # writes to virtual pin 5 and data sent is the value of the variable motion
    temperatureDs18b20 = sensor.get_temperature() # sets the variable temperatureDs18b20 to the value of the sensor reading
    blynk.virtual_write(6,temperatureDs18b20) #writes to virtual pin 6 and data sent is the value of the variable temperatureDs18b20
    if motion == 1: # this checks if a motion has occurred ,when the value is 1
        currentTime = datetime.datetime.now().strftime("%H:%M:%S") #gets current time 
        text= f"""Hi,\n there has been some motion observed from the baby at {currentTime}. Please log into the BabyCam App to view a live feed of the camera or ask alexa to show you the baby camera using the command 'Alexa start Voice Monkey'.
        \n
        From the BabyCam Team """ # text that is the body of the email
        send_mail('BabyCamPi@pi.ie', '20099854@mail.wit.ie', 'Motion Detected from BabyCam Pi',text)
        logging.info("motion detected") #logs an event on the blynk app
        blynk.log_event("motion_detected",f"The baby Camera has detected motion with your baby at {currentTime} please log into the app to view the camera") #this is the event that becomes the notification 
        print(f"motion detected waiting 90 secs to resume")
        sleep(90) 
    else: 
        sleep(2)  
except KeyboardInterrupt:
  GPIO.cleanup()
  print('GPIO Good to Go')