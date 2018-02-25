import RPi.GPIO as GPIO
import time

UP_GPIO = 23
DOWN_GPIO = 24
RIGHT_GPIO = 25
LEFT_GPIO = 16
RIGHT_EYE_GPIO = 18
LEFT_EYE_GPIO = 21

def init_pins():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(UP_GPIO, GPIO.OUT)
	GPIO.setup(DOWN_GPIO, GPIO.OUT)
	GPIO.setup(RIGHT_GPIO, GPIO.OUT)
	GPIO.setup(LEFT_GPIO, GPIO.OUT)
	GPIO.setup(RIGHT_EYE_GPIO, GPIO.OUT)
	GPIO.setup(LEFT_EYE_GPIO,GPIO.OUT)


	GPIO.output(RIGHT_EYE_GPIO, GPIO.HIGH)
	GPIO.output(LEFT_EYE_GPIO ,GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(RIGHT_EYE_GPIO, GPIO.LOW)
	GPIO.output(LEFT_EYE_GPIO,GPIO.LOW)


def up(setting):
	GPIO.output(UP_GPIO, GPIO.HIGH)
	time.sleep(setting)
	GPIO.output(UP_GPIO, GPIO.LOW)

def down(setting):
	GPIO.output(DOWN_GPIO, GPIO.HIGH)
	time.sleep(setting)
	GPIO.output(DOWN_GPIO, GPIO.LOW)


def left(setting):
	GPIO.output(UP_GPIO, GPIO.HIGH)
	GPIO.output(LEFT_GPIO, GPIO.HIGH)
	time.sleep(setting)
	GPIO.output(UP_GPIO, GPIO.LOW)
	GPIO.output(LEFT_GPIO, GPIO.LOW)

def right(setting):
	GPIO.output(UP_GPIO, GPIO.HIGH)
	GPIO.output(RIGHT_GPIO, GPIO.HIGH)
	time.sleep(setting)
	GPIO.output(UP_GPIO, GPIO.LOW)
	GPIO.output(RIGHT_GPIO, GPIO.LOW)


def light(settings):
	if(settings == True):
		GPIO.output(RIGHT_EYE_GPIO, GPIO.HIGH)
		GPIO.output(LEFT_EYE_GPIO,GPIO.HIGH)
	else:
		GPIO.output(RIGHT_EYE_GPIO, GPIO.LOW)
		GPIO.output(LEFT_EYE_GPIO,GPIO.LOW)

def moving(setting):
	if(setting == "up"):
		GPIO.output(UP_GPIO, GPIO.HIGH)
	elif(setting == "down"):
		GPIO.output(DOWN_GPIO, GPIO.HIGH)
	elif(setting == "left"):
		GPIO.output(UP_GPIO, GPIO.HIGH)
		GPIO.output(LEFT_GPIO, GPIO.HIGH)
	elif(setting == "right"):
		GPIO.output(UP_GPIO, GPIO.HIGH)
		GPIO.output(RIGHT_GPIO, GPIO.HIGH)

def wait(settings):
	time.sleep(settings)

def stop(settings):
	GPIO.output(UP_GPIO, GPIO.LOW)
	GPIO.output(DOWN_GPIO, GPIO.LOW)
	GPIO.output(LEFT_GPIO, GPIO.LOW)
	GPIO.output(RIGHT_GPIO, GPIO.LOW)
