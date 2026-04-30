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

try:
    while True:
        GPIO.output(RED_PIN, GPIO.HIGH)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        time.sleep(5)

        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.LOW)
        GPIO.output(GREEN_PIN, GPIO.HIGH)
        time.sleep(5)

        GPIO.output(RED_PIN, GPIO.LOW)
        GPIO.output(YELLOW_PIN, GPIO.HIGH)
        GPIO.output(GREEN_PIN, GPIO.LOW)
        time.sleep(3)

except KeyboardInterrupt:
    print("Stopping traffic light")

finally:
    GPIO.cleanup()
