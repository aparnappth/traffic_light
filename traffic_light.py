import RPi.GPIO as GPIO
import time

RED_PIN = 22
YELLOW_PIN = 27
GREEN_PIN = 18
BUTTON_PIN = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pedestrian_requested = False


def set_light(red, yellow, green):
    GPIO.output(RED_PIN, GPIO.HIGH if red else GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.HIGH if yellow else GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH if green else GPIO.LOW)


def check_button():
    global pedestrian_requested

    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        pedestrian_requested = True


def wait_and_check(seconds):
    start_time = time.time()

    while time.time() - start_time < seconds:
        check_button()
        time.sleep(0.1)


def run_state(state):
    global pedestrian_requested

    if state == "RED":
        set_light(True, False, False)
        wait_and_check(3)

        if pedestrian_requested:
            pedestrian_requested = False
            return "RED_PEDESTRIAN"

        return "GREEN"

    if state == "GREEN":
        set_light(False, False, True)
        wait_and_check(3)
        return "YELLOW"

    if state == "YELLOW":
        set_light(False, True, False)
        wait_and_check(1)
        return "RED"

    if state == "RED_PEDESTRIAN":
        set_light(True, False, False)
        print("Pedestrian crossing")
        wait_and_check(5)
        return "GREEN"


try:
    current_state = "RED"

    while True:
        current_state = run_state(current_state)

except KeyboardInterrupt:
    print("Stopping traffic light")

finally:
    set_light(False, False, False)
    GPIO.cleanup()
