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


def run_state(state):
    if state == "RED":
        set_light(True, False, False)
        time.sleep(3)
        return "GREEN"

    if state == "GREEN":
        set_light(False, False, True)
        time.sleep(3)
        return "YELLOW"

    if state == "YELLOW":
        set_light(False, True, False)
        time.sleep(1)
        return "RED"


try:
    current_state = "RED"

    while True:
        current_state = run_state(current_state)

except KeyboardInterrupt:
    print("Stopping traffic light")

finally:
    set_light(False, False, False)
    GPIO.cleanup()
