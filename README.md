<h1 align="center">Serial Connection</h1>

<p>'<b>SerialConnection</b>' is a Python class for serial communication, which provides a simple interface for reading and writing data to a serial port. The class is designed to be easy to use and can be customized for different baud rates and ports.</p>

The class provides four methods: '<b>open()</b>', '<b>read()</b>', '<b>write()</b>', and '<b>close()</b>', which correspond to the basic operations of opening a serial port, reading data from it, writing data to it, and closing the connection.

<p>The class also includes an error method that returns any error messages generated during the operation of the class. The error messages can be used to diagnose and fix issues during serial communication.</p>

The code is compatible with both Windows and Linux, making it a useful tool for anyone working with serial devices.

<p>Use this code to quickly and easily integrate serial communication into your Python project.</p>


<h2>Installation</h2>

<p>To use this library, you must have Python 3.6 or later installed on your system. You can <a href="https://www.python.org/downloads/" target="_blank">download</a> Python from the official website.</p>

You can install the pyserial module, which is used by this library, using pip. Open a terminal or command prompt and type:

<p>Copy code</p>
pip install pyserial

<p>Once you have Python and pyserial installed, you can use this library in your Python projects.</p>

<h2>Usage</h2>

<table>
	<tr>
    	<td>1. Import the '<b>SerialConnection</b>' class:<p>&nbsp;</p></td>
	</tr>	  
	<tr>
    	<td><img src="screens/1.jpg" alt="Screenshot 1"></td>
	</tr>	  
	<tr>
		<td><p>&nbsp;</p><p>2. Create a new instance of '<b>SerialConnection</b>' by passing the port and baudrate as parameters: </p><p>&nbsp;</p></td>
	</tr>	  
	<tr>
    	<td><img src="screens/2.jpg" alt="Screenshot 2"></td>
	</tr>	  
	<tr>
    	<td><p>&nbsp;</p><p>3. Open the serial port:</p><p>&nbsp;</p></td>
	</tr>	  
	<tr>
    	<td><img src="screens/3.jpg" alt="Screenshot 3"></td>
	</tr>	  
	<tr>
    	<td><p>&nbsp;</p><p>4. Write data to the serial port:</p><p>&nbsp;</p></td>
	</tr>	  
	<tr>
    	<td><img src="screens/4.jpg" alt="Screenshot 4"></td>
	</tr>	  
	<tr>
    	<td><p>&nbsp;</p><p>5. Read data from the serial port:</p><p>&nbsp;</p></td>
	</tr>	
	<tr>
    	<td><img src="screens/5.jpg" alt="Screenshot 5"></td>
	</tr>	
	<tr>
    	<td><p>&nbsp;</p><p>6. Close the serial port:</p><p>&nbsp;</p></td>
	</tr>	
	<tr>
    	<td><img src="screens/6.jpg" alt="Screenshot 6"></td>
	</tr>	
	<tr>
    	<td><p>&nbsp;</p><p>Note: '<b>device.error()</b>' returns a string with the last error message.</p><p>&nbsp;</p></td>
	</tr>
</table>

<h2>Contributions</h2>

<p>If you find any bugs or issues with '<b>SerialConnection</b>', please feel free to report them by opening an issue on this repository.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the LICENSE.md file for more information.</p>

<h2>Connect with me:</h2>

<p>
If you have any questions, feedback or just want to connect, feel free to reach out to me on LinkedIn.
</p>

<a href="https://linkedin.com/in/marco-alexandre-serrano" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="marco-alexandre-serrano" height="30" width="40" /></a>
