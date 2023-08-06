import serial
import socket


class Connect:
    def __init__(self, connections=2, data_method=None, com=None, port=None, exe_location=None):
        self.ser = None
        self.mainSocket = None

        if connections == 2 or connections == 4:
            self.connections = connections
        else:
            raise Exception('Value for connections must be either 2 or 4.')

        data_method = data_method.lower().strip()

        if data_method == 'com' or data_method == 'socket' or data_method == 'exe':
            self.data_method = data_method
            self.com = com
            self.port = port
            self.exe_location = exe_location
        else:
            raise Exception('Value for data_method must be com, socket or exe.')

        if self.data_method == 'com':
            if self.com is None or not isinstance(self.com, str):
                raise Exception('When data_method value is com... com must have a string value.')
        elif self.data_method == 'socket':
            if self.port is None or not isinstance(self.port, int):
                raise Exception('When data_method value is socket... port must have a integer value.')
        elif self.data_method == 'exe':
            if self.exe_location is None or not isinstance(self.exe_location, str):
                raise Exception('When data_method value is exe... exe_location must have a string value.')

    def init(self):
        if self.data_method == 'com':
            port = "\\\\.\\" + str(self.com)
            self.ser = serial.Serial(port, 4608000, timeout=0)
        elif self.data_method == 'socket':
            self.mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname(socket.gethostname())
            self.mainSocket.connect((remote_ip, self.port))
        elif self.data_method == 'exe':
            return

    def read_line(self, do_check=True):
        if self.data_method == 'com':
            if (do_check and self.size() > 30) or not do_check:
                return self.ser.readline()
            else:
                return
        elif self.data_method == 'socket':
            return self.mainSocket.recv(1024)
        elif self.data_method == 'exe':
            return

    def get_cords(self, do_check=True):
        read = self.read_line(do_check)
        if read is not None:
            tmp = read.decode().split(',')

            if len(tmp) == self.connections:
                return list(map(float, tmp))
            else:
                return []
        else:
            return []

    def size(self):
        if self.data_method == 'com':
            return self.ser.inWaiting()
        elif self.data_method == 'socket':
            raise Exception("This function size is not available for this data_method")
        elif self.data_method == 'exe':
            raise Exception("This function size is not available for this data_method")

    def flush(self):
        if self.data_method == 'com':
            self.ser.flush()
        elif self.data_method == 'socket':
            raise Exception("This function flush is not available for this data_method")
        elif self.data_method == 'exe':
            raise Exception("This function flush is not available for this data_method")
