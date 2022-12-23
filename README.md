# BabyCam 
This is a repository for an IoT BabyCam on a Raspberry Pi by Ayodele Onamusi 20099854 WIT HDip Comp Sci Computer Networking project

# Features
The Babycam uses the raspberry pi model 3b+ along with a 
  1. SenseHat
  2. PiCamera
  3. DS18B20 temperature sensor
  4. PIR HC-SR501 motion detector sensor
  5. Canakit Raspberry Pi GPIO Breakout board
  6. Canakit Ribbon Cable
  7. Jumper wires
  8. Raspberry Pi 40 Pin GPIO 1 to 2 expansion board
  9. Mobile Phone Device
  10. Amazon Echo 8

* The Device allows the user to be able to use their mobile phone to view their baby who may be in another room via the blynk app.
* The Device also sends data on the latest room temperature and humidity to the app.
* The Device also notes if the baby moves and sends a notification to the mobile app and also sends an email.
* The User can also summon the live stream of the baby cam from alexa devices within the house.

# Video:
A video of the operations of this IoT BabyCam which includes a code walkthrough , and a live demo of the product with how it was put together can be found on youtube by following this link : https://youtu.be/o-bwmK9FOGI 

# Instructions:
To use the BabyCam , you will need to run the mjpg-streamer first , by going into the BabyCam/mjpg-streamer/mjpg-streamer-experimental folder and running the following commands :
1. export LD_LIBRARY_PATH=. 
then
2. ./mjpg_streamer  -i "input_uvc.so"

This will stream the video on your local network at{raspberrypiIPaddress}:8080/?action=stream

In a separate terminal window run the babycam.py script in python3. 
This would load the sensor data.
Open the blynk app and open the device corresponding to the device key you put in the babycam.py script under blynk_auth







 


