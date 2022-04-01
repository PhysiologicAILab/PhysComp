from ast import Str
import serial
import serial.tools.list_ports as lp

class serialPort():
    def __init__(self) -> None:
        self.ser = serial.Serial()
        self.baudrate = 9600
        self.timeout = 10  # specify timeout when using readline()
        self.ports = lp.comports()

    def connectPort(self, port_name):
        self.ser.port = port_name  # "/dev/cu.usbmodem14101" # 'COM3'  # Arduino serial port
        self.ser.baudrate = self.baudrate
        self.ser.timeout = self.timeout  # specify timeout when using readline()

        self.ser.open()
        return self.ser.is_open

    def disconnectPort(self):
        self.ser.close()
        return
