import RPi.GPIO as GPIO
import time

RED_PIN = 22
YELLOW_PIN = 27
GREEN_PIN = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)


def set_light(red, yellow, green):
    GPIO.output(RED_PIN, GPIO.HIGH if red else GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.HIGH if yellow else GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH if green else GPIO.LOW)


try:
    while True:
        set_light(True, False, False)   # Red ON
        time.sleep(3)

        set_light(False, False, True)   # Green ON
        time.sleep(3)

        set_light(False, True, False)   # Yellow ON
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping traffic light")

finally:
    set_light(False, False, False)
    GPIO.cleanup()
