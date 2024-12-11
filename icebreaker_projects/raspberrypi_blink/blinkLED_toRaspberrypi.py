import RPi.GPIO as GPIO
import time

# Pin configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)  # GPIO 17 for output

try:
    while True:
        GPIO.output(17, GPIO.HIGH)  # Send HIGH signal
        time.sleep(1)  # 1-second delay
        GPIO.output(17, GPIO.LOW)   # Send LOW signal
        time.sleep(1)  # 1-second delay
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on CTRL+C
