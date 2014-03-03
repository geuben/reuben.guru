import serial
from xbee import ZigBee

serial_port = serial.Serial('/dev/ttyAMA0', 9600)
xbee = ZigBee(serial_port, escaped=True)

while True:
  print xbee.wait_read_frame()
