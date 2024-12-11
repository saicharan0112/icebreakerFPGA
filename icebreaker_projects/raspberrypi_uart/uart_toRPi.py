import serial

# Open UART port
ser = serial.Serial('/dev/serial0', 115200, timeout=1)  # Adjust if necessary

while True:
    if ser.in_waiting > 0:
        data = ser.read(ser.in_waiting).decode()
        print(f"Received: {data}")
