import serial
from pythonosc.udp_client import SimpleUDPClient

class ArduinoOscInput:
	def __init__(self, ip="127.0.0.1", client, osc_address="/ard/sensor1", osc_port=7000, serial_device='/dev/tty.usbmodem14201', baud_rate=19200):
		self.CLIENT_IP = ip
		self.osc_address = osc_address
		self.osc_port = osc_port
		self.serial_device = serial_device
		self.baud_rate = baud_rate


	def start(self):
	    print(f"OSC UDP client sending to {self.client_ip} on port {self.osc_address}, address: {self.osc_address}")
	    print(f"Connecting to serial at {self.serial_device} with baud {self.baud_rate}")
	    self.osc_client = SimpleUDPClient(self.client_ip, self.osc_port)
	    self.ser = serial.Serial(self.serial_device, baudrate=self.baud_rate, timeout=None)
	    self.ser.flushInput()

	    while True:
	        try:
	            ser_bytes = self.ser.readline()
	            # print(ser_bytes)
	            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
	            # Send a float through OSC
	            self.osc_client.send_message(self.osc_address, decoded_bytes)
	            print(decoded_bytes)
	            # with open("test_data.csv","a") as f:
	            #     writer = csv.writer(f,delimiter=",")
	            #     writer.writerow([time.time(),decoded_bytes])
	        except:
	            print("Keyboard interrupt!")
	            break

if __name__ == "__main__":
	app = ArduinoOscInput()
	app.start()