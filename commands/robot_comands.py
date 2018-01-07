import RPi.GPIO as GPIO
import time

IS_INIT=False

def init_pins():
	GPIO.setmode(GPIO.BCM)
	#backward
	GPIO.setup(23, GPIO.OUT)
	#forward
	GPIO.setup(24, GPIO.OUT)
	#right
	GPIO.setup(25, GPIO.OUT)
	#left
	GPIO.setup(16, GPIO.OUT)
	#right eye
	GPIO.setup(18, GPIO.OUT)
	#left eye
	GPIO.setup(21,GPIO.OUT)
	IS_INIT=True

def direction(setting):
	if(setting == "up"):
		GPIO.output(24, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(24, GPIO.LOW)

	elif(setting == "down"):
		GPIO.output(23, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(23, GPIO.LOW)

	elif(setting == "left"):
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(16, GPIO.LOW)

	elif(setting == "right"):
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(24, GPIO.LOW)
		GPIO.output(25, GPIO.LOW)

def light(settings):
	print ("Here")
	if(settings == True): 
		GPIO.output(18, GPIO.HIGH)
		GPIO.output(21,GPIO.HIGH)
	else:
		GPIO.output(18, GPIO.LOW)
		GPIO.output(21,GPIO.LOW)

def moving(setting):
	if(setting == "up"):
		GPIO.output(24, GPIO.HIGH)
	elif(setting == "down"):
		GPIO.output(23, GPIO.HIGH)
	elif(setting == "left"):
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(16, GPIO.HIGH)
	elif(setting == "right"):
		GPIO.output(24, GPIO.HIGH)
		GPIO.output(25, GPIO.HIGH)

def stop(settings):
	GPIO.output(16, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
