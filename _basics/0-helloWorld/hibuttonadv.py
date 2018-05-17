import RPi.GPIO as GPIO


def button_callback(channel):
    print("Button %s was pushed!" % channel)


def set_pin_data(channel):
    #GPIO.setup(channel, GPIO.IN)
    GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # set initial value to be pulled low (off)
    GPIO.add_event_detect(channel, GPIO.RISING, callback=button_callback)
    print("channel %s active" % channel)


pinA = 26
pinB = 19

GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)  # Ignore warning for now
set_pin_data(pinA)
set_pin_data(pinB)
message = input("Press enter to quit\n\n")  # Run until someone presses enter
GPIO.cleanup()  # Clean up
