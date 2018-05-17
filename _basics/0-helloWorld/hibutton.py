# EJEMPLO DE BLINKING CON RASPBERRY PI
# Escrito por Gl4r3
import RPi.GPIO as GPIO  # importamos la libreria y cambiamos su nombre por "GPIO"
import time  # necesario para los delays

# establecemos el sistema de numeracion que queramos, en mi caso BCM
GPIO.setmode(GPIO.BCM)

# configuramos el pin GPIO17 como una salida
# GPIO.setup(26, GPIO.IN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
counter = 1

while True:
    if GPIO.input(26):
        print("Apretado!!!" + str(counter))
        counter = counter+1

GPIO.cleanup()  # devuelve los pines a su estado inicial
