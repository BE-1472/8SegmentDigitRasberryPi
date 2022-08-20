
import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay
import array

GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  

pinNumbersArray = array.array('i', [21, 20, 16, 12, 26, 19, 13, 22])

GPIO.setup(21 ,GPIO.OUT)           # Decimal point
GPIO.setup(20 ,GPIO.OUT)           #
GPIO.setup(16 ,GPIO.OUT)           #
GPIO.setup(12 ,GPIO.OUT)           #

GPIO.setup(26 ,GPIO.OUT)           #
GPIO.setup(19 ,GPIO.OUT)           #
GPIO.setup(13 ,GPIO.OUT)           #
GPIO.setup(22 ,GPIO.OUT)           #

def drawZero():
    GPIO.output(19, 1)
    GPIO.output(13, 1)
    GPIO.output(12, 1)
    GPIO.output(16, 1)
    GPIO.output(20, 1)
    GPIO.output(26, 1)
    
def drawOne():
    
def drawTwo():

def drawThree():

def drawFour():

def drawFive():

def drawSix():

def drawSeven():

def drawEight():

def drawNine():

def clearDigit()
    for i in pinNumbersArray:
    GPIO.output(i, 0)
    
def loopThroughPins()
        GPIO.output(21, 1)
        sleep(timeDelimiter)
        GPIO.output(21, 0)
        sleep(timeDelimiter)
        GPIO.output(20, 1)
        sleep(timeDelimiter)
        GPIO.output(20, 0)
        sleep(timeDelimiter)
        GPIO.output(16, 1)
        sleep(timeDelimiter)
        GPIO.output(16, 0)
        sleep(timeDelimiter)
        GPIO.output(12, 1)
        sleep(timeDelimiter)
        GPIO.output(12, 0)
        sleep(timeDelimiter)
        GPIO.output(26, 1)
        sleep(timeDelimiter)
        GPIO.output(26, 0)
        sleep(timeDelimiter)
        GPIO.output(19, 1)
        sleep(timeDelimiter)
        GPIO.output(19, 0)
        sleep(timeDelimiter)
        GPIO.output(13, 1)
        sleep(timeDelimiter)
        GPIO.output(13, 0)
        sleep(timeDelimiter)
        GPIO.output(22, 1)
        sleep(timeDelimiter)
        GPIO.output(22, 0)
        sleep(timeDelimiter)
    
timeDelimiter = 1.0

try:  
    while True:  
        loopThroughPins()
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
