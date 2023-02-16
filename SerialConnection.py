'''

############################################################################################
####    MIT License                                                                     ####
####                                                                                    ####
####    Copyright (c) 2023 marcoserrano1980                                             ####
####                                                                                    ####
####    Permission is hereby granted, free of charge, to any person obtaining a copy    ####
####    of this software and associated documentation files (the "Software"), to deal   ####
####    in the Software without restriction, including without limitation the rights    ####
####    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell       ####
####    copies of the Software, and to permit persons to whom the Software is           ####
####    furnished to do so, subject to the following conditions:                        ####
####                                                                                    ####
####    The above copyright notice and this permission notice shall be included in all  ####
####    copies or substantial portions of the Software.                                 ####
####                                                                                    ####
####    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR      ####
####    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,        ####
####    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE     ####
####    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER          ####
####    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,   ####
####    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE   ####
####    SOFTWARE.                                                                       ####
####                                                                                    ####
####    Developed by Marco Serrano                                                      ####
####    https://www.linkedin.com/in/marco-alexandre-serrano                             ####
####    https://github.com/marcoserrano1980                                             ####
####    marco.a.s.serrano@gmail.com                                                     ####
####                                                                                    ####
############################################################################################

class SerialConnection:
    Initialize:
        port as a string
        baudrate as an integer
        serial as None
        error as an empty string
        
    Method: Return error message
        return error
        
    Method: Open serial port
        if serial is None:
            try:
                create a serial object with port and baudrate
            except serial.SerialException as e:
                set error message and return False
            else:
                return True
        else:
            set error message, port is already open and return False
            
    Method: Read from serial port
        if serial is not None:
            try:
                read from the serial port, decode the bytes and return as a string
            except serial.SerialException as e:
                set error message and return False
            else:
                return data
        else:
            set error message, port is not open and return False
        
    Method: Write to serial port
        if serial is not None:
            try:
                encode the string data to bytes and write to serial port
            except serial.SerialException as e:
                set error message and return False
            else:
                return True
        else:
            set error message, port is not open and return False
        
    Method: Close serial port
        if serial is not None:
            try:
                close the serial connection and set serial to None
            except serial.SerialException as e:
                set error message and return False
            else:
                return True
        else:
            set error message, port is not open and return False


'''

import serial

class SerialConnection:

    # Constructor 
    def __init__(self, port, baudrate):
        self.port = port          # Port to connect to
        self.baudrate = baudrate  # Baud rate for serial communication
        self.serial = None        # Serial object to be instantiated
        self._error = ''          # Private variable to store any error messages

    # Return error message 
    def error(self):
        return self._error

    # Open serial port
    def open(self):
        # Check if the serial port is not already open
        if self.serial is None:
            try:
                # Instantiate the serial object
                self.serial = serial.Serial(self.port, self.baudrate)
            except serial.SerialException as e:
                # Set error message
                self._error = f"Failed to open serial port '{self.port}': {e}"
                return False
            else:
                return True
        else:
            # Set error message, port is already open
            self._error = f"Serial port '{self.port}' is already open."
            return False

    # Read serial port
    def read(self, size=1):
        # Check if the serial port is open
        if self.serial is not None:
            try:
                # Read from serial and decode the bytes to string
                data = self.serial.readline(size=size).strip().decode('utf-8')
            except serial.SerialException as e:
                # Set error message if any problem
                self._error = f"Failed to read from serial port '{self.port}': {e}"
                return False
            else:
                return data
        else:
            # Set error message, port is not open
            self._error = f"Serial port '{self.port}' is not open."
            return False

    # Write a message into a serial port
    def write(self, data):
        # Check if the serial port is open
        if self.serial is not None:
            try:
                # Encode the string message into bytes and write to serial
                self.serial.write(data.encode())
            except serial.SerialException as e:
                # Set error message if any problem
                self._error = f"Failed to write to serial port '{self.port}': {e}"
                return False
            else:
                return True
        else:
            # Set error message, port is not open
            self._error = f"Serial port '{self.port}' is not open."
            return False

    # Close serial port
    def close(self):
        # Check if the serial port is open
        if self.serial is not None:
            try:
                # Close the serial connection and set serial object to None
                self.serial.close()
                self.serial = None
            except serial.SerialException as e:
                # Set error message if any problem
                self._error = f"Failed to close serial port '{self.port}': {e}"
                return False
            else:
                return True
        else:
            # Set error message, port is not open
            self._error = f"Serial port '{self.port}' is not open."
            return False


# Create a new SerialConnection object with port '/dev/ttyUSB0' and baudrate 9600,
# and try to open it. Assign the value of the return statement to the 'device' variable.
#if device = SerialConnection('/dev/ttyUSB0', 9600).open() != True:
#    print(device.error())
#
# Try to open the serial connection. If opening the connection fails, print the error message.
#if device.open() != True:
#    print(device.error())
#
# Try to write the message 'Hello, device 1!' to the serial connection.
# If writing to the connection fails, print the error message.
#if device.write('Hello, device 1!') != True:
#    print(device.error())
#
# Try to read data from the serial connection. If reading data fails,
# print the error message. If reading data succeeds, print the data.
#data = device.read()
#if (data = device.read()) != False:
#    print('Device data:', data)
#else:
#    print(device.error())
#
# Try to close the serial connection. If closing the connection fails,
# print the error message.
#if device.close() != True:
#    print(device.error())