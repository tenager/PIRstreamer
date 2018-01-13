import time
import picamera
import os
import sys
import RPi.GPIO as GPIO

# define PIR pin
PIR_PIN = 4

# give your server ip address
server_ip_address = "192.168.1.177"

def my_callback(PIR_PIN):
        print "\n motion detected"
        print "\n Start recording video ..."
        #initialize camera
        time.sleep(1)
        streaming_application()

def streaming_application():
       # stream video data over netcat over port 8000
        os.system("raspivid -n -w 680 -h 420 -fps 25 -t 60000 -o - | nc "+server_ip_address+" 8000")

def main():
        print "Video surveillance application."
        print "Press CTRL+C to exit"
        print "No motion ..."
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=my_callback, bouncetime=12000)
        while 1:
                time.sleep(100)
        GPIO.cleanup()

# if this script is run directly on the terminal using command line
# run the main() function of the code
if __name__== "__main__":
        main()

