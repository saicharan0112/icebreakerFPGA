import serial, time

# Open UART port
# ser = serial.Serial('/dev/serial0', 115200)

# Test Loopback
# try:
#     while True:
#         test_message = "Hello, FPGA!\n"
#         ser.write(test_message.encode())  # Send message
#         time.sleep(1)
#         print(test_message)

#         response = ser.read(len(test_message))  # Read back
#         print("FPGA Response:", response.decode())
# except:
#     print("Ctrl C")


# Configure the serial port
# ser = serial.Serial('/dev/ttyUSB0', 115200)  # Replace with your serial port and baud rate

# Data to send
# message = b"Hello, FPGA!"

# Transmit data
# ser.write(message)

# Close the serial port
# ser.close()


import RPi.GPIO as GPIO

# Pin configuration
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN)
GPIO.setup(26, GPIO.IN)
    
try:
    while True:
        print("Transmitted "+str(GPIO.input(16)))
        time.sleep(1)
        print("Received "+str(GPIO.input(26)))
except:
    print("Ctrl C")