#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
def readRfid():
    #GPIO.cleanup()
    reader = SimpleMFRC522()

    try:
            id, text = reader.read()
            text=text.rstrip()
    finally:
            GPIO.cleanup()
    return text


