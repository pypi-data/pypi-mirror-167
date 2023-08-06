from typing import Any

import serial
import socket


class Connect:
    """
    The Connect class makes it easier to connect to the 2 or 4 connection CTS to get live data.
    """

    def __init__(self, connections=2, data_method=None, com=None, port=None, exe_location=None):
        """
        Arguments:
        - connections (int req): States if you are connecting to either a 2 or 4 connection CTS.
        - data_method (str req): States what data retrieval method is being used. Either 'com',
        'socket', or 'exe'.
        - com (str): Value of COM point to connect to (ex. 'COM3'). Required if data_method is 'com'.
        - port (int): Value of socket port to connect to (ex. 8888). Required if data_method is 'socket'.
        - exe_location (str): Value of location to visual_backend_v1.exe
        (ex. 'c:/Users/user/Desktop/visual_backend_v1.exe'). Required if data_method is 'exe'.
        """

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
        """
        Sets up the Connect class and returns the class. A required step before running any functions.
        """

        if self.data_method == 'com':
            port = "\\\\.\\" + str(self.com)
            self.ser = serial.Serial(port, 4608000, timeout=0)
        elif self.data_method == 'socket':
            self.mainSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = socket.gethostbyname(socket.gethostname())
            self.mainSocket.connect((remote_ip, self.port))
        elif self.data_method == 'exe':
            return Exception("The data_method exe has not been implemented yet")

        return self

    def read_line(self, do_check=True) -> str | Exception | None:
        """
        Returns string of the latest data from the CTS. Returns None if no data is there.

        Arguments:
        - do_check (bool): Default is True. This value indicates if data_method is 'com' that it will check
        if there is data to return.
        """

        if self.data_method == 'com':
            if (do_check and self.size() > 30) or not do_check:
                return self.ser.readline()
            else:
                return None
        elif self.data_method == 'socket':
            return self.mainSocket.recv(1024)
        elif self.data_method == 'exe':
            return Exception("The data_method exe has not been implemented yet")

    def get_cords(self, do_check=True) -> [float]:
        """
        Returns array of the latest data from the CTS. Returns empty array if no data is there.

        Arguments:
        - do_check (bool): Default is True. This value indicates if data_method is 'com' that it will check
        if there is data to return.
        """

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
        """
        Only if data_method is 'com' return the bytes (int) waiting in the queue.
        """

        if self.data_method == 'com':
            return self.ser.inWaiting()
        else:
            raise Exception("This function size is not available for this data_method")

    def flush(self):
        """
        Only if data_method is 'com' flush the data waiting in queue.
        """

        if self.data_method == 'com':
            self.ser.flush()
        else:
            raise Exception("This function flush is not available for this data_method")

    def end(self):
        """
        End process of receiving data for cts. If any functions are run after this they will throw
        errors.
        """

        if self.data_method == 'com':
            self.ser.close()
        elif self.data_method == 'socket':
            self.mainSocket.close()
        elif self.data_method == 'exe':
            return Exception("The data_method exe has not been implemented yet")
