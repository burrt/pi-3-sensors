"""
Very simple blinker for LEDs using input GPIO pins or defaults to GPIO18
"""
import sys
import time
import RPi.GPIO as GPIO

DEFAULT_GPIO_PIN = 18
TOGGLE_DELAY = 4

def main():
    pins = sys.argv[1:]

    # Disable warnings and set gpio pin type
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Loop over all GPIO pins and toggle high/low
    try:
        while True:
            if pins:
                for gpio_pin in pins:
                    toggle_led(int(gpio_pin))
            else:
                toggle_led(DEFAULT_GPIO_PIN)
            time.sleep(TOGGLE_DELAY)

    # On Ctrl+C, turn all LEDs off
    except KeyboardInterrupt:
        if pins:
            for gpio_pin in pins:
                GPIO.setup(gpio_pin, GPIO.OUT)
                GPIO.output(gpio_pin, GPIO.LOW)
        else:
            GPIO.setup(DEFAULT_GPIO_PIN, GPIO.OUT)
            GPIO.output(DEFAULT_GPIO_PIN, GPIO.LOW)

def toggle_led(pin_num):
    GPIO.setup(pin_num, GPIO.OUT)

    print("[{0}] - LED on".format(pin_num))
    GPIO.output(pin_num, GPIO.HIGH)

    GPIO.setup(pin_num, GPIO.OUT)
    time.sleep(TOGGLE_DELAY)

    print("[{0}] - LED off".format(pin_num))
    GPIO.output(pin_num, GPIO.LOW)

if __name__ == "__main__":
    main()
