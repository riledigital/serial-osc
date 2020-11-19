import serial
from pythonosc.udp_client import SimpleUDPClient

CLIENT_IP = "127.0.0.1"
# CLIENT_IP = "localhost"
OSC_PORT = 7000
OSC_ADDRESS = "/arduino/sensor1"
osc_client = SimpleUDPClient(CLIENT_IP, OSC_PORT)

SERIAL_DEVICE = '/dev/tty.usbmodem14201'
BAUD_RATE = 19200

if __name__ == "__main__":
    print(f"OSC UDP client sending to {CLIENT_IP} on port {OSC_PORT}, address: {OSC_ADDRESS}")
    print(f"Connecting to serial at {SERIAL_DEVICE} with baud {BAUD_RATE}")
    ser = serial.Serial(SERIAL_DEVICE, baudrate=BAUD_RATE,timeout=None)
    ser.flushInput()

    while True:
        try:
            ser_bytes = ser.readline()
            # print(ser_bytes)
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
