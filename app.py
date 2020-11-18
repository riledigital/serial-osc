import serial
from pythonosc.udp_client import SimpleUDPClient

CLIENT_IP = "127.0.0.1"
PORT = 1337
OSC_ADDRESS = "/arduino/sensor1"
osc_client = SimpleUDPClient(CLIENT_IP, PORT)

SERIAL_DEVICE = '/dev/ttyACM0'

ser = serial.Serial(SERIAL_DEVICE)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        # Send a float through OSC
        osc_client.send_message(OSC_ADDRESS, decoded_bytes)
        print(decoded_bytes)
        # with open("test_data.csv","a") as f:
        #     writer = csv.writer(f,delimiter=",")
        #     writer.writerow([time.time(),decoded_bytes])
    except:
        print("Keyboard Interrupt")
        break