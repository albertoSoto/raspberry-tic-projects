import RPi.GPIO as GPIO
import time

currentPort = 17
sleepTime = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

for x in range(0, 3):
    print("We're on time %d" % (x))
    GPIO.output(currentPort, True)
    time.sleep(sleepTime)
    GPIO.output(currentPort, False)
    time.sleep(sleepTime)

print("Done")
GPIO.cleanup()
