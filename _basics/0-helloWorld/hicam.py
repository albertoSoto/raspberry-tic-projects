import time
import picamera

camera = picamera.PiCamera()
try:
    camera.vflip = True #Vertical flip to work properly with touchscreen
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()
finally:
    camera.close()