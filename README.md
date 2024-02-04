# MicroPython Project for Teen Tech Center at OMSI

This project involves the use of the Pico Pi board and the Thonny Integrated Development Environment. Please follow the subsequent instructions properly and carefully to successfully set up your project environment.

## Installation Instructions

### MicroPython
Install micropython using this [documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)

### Thonny IDE

Thonny is a Python IDE for beginners which will help us interact with the Pico Pi board. 

1. Download and install Thonny IDE from here: https://thonny.org/
2. Once installed, open Thonny IDE.
3. For communication with the Raspberry Pi Pico, go to the `Tools > Options > Interpreter` and select `MicroPython (Raspberry Pi Pico)`.

### Raspberry Pi Pico

Raspberry Pi Pico is a microcontroller board based on the Raspberry Pi RP2040 microcontroller chip.

1. Plug your Pi Pico into the USB port of your computer.
2. It will appear as a removable drive.
3. In the Thonny IDE, you can now directly open files from the Pico and save files to it.

## Project Setup

### secrets.py

Create a `secrets.py` file in the Thonny IDE to store the WiFi SSID and password.

```python
ssid = "your_wifi_ssid"
password = "your_wifi_password"
```
Replace `"your_wifi_ssid"` and `"your_wifi_password"` with your actual WiFi credentials. This file should not be shared or made public for security reasons.

## Running the Code

Copy and paste the provided `install.py` and `server.py` code into your Thonny IDE files, save them, and then run install.py before running server.py.

Note: If the LED does not light up when the Pi Pico is connected to WiFi, please check your internet connection and make sure that the Raspberry Pi Pico can communicate with the internet.

 This Python code is utilizing a number of modules to connect to a Wi-Fi and 
  deliver a server that can toggle an LED on or off over the internet.        
                                                                              
  The first couple of lines of the code are importing necessary modules.      
                                                                              
    from secret import ssid, password                                         
    from phew import server, connect_to_wifi, get_ip_address                  
    from machine import Pin                                                   
                                                                              
  •  secret  module contains the network's SSID and password, which are       
  required for Wi-Fi connection.                                              
  •  phew  module provides a lightweight Python HTTP server, as well as two   
  utility functions for connecting to Wi-Fi and getting the IP address.       
  •  machine  module is used to interact with hardware components. Here, it's 
  used to control an LED.                                                     
                                                                              
  Next, an LED object is defined which is set to output mode.                 
                                                                              
    led = Pin("LED", Pin.OUT)                                                 
                                                                              
  The LED is referred by its name ("LED"). The argument  Pin.OUT  means that  
  the pin setting is defined to output mode which means it can output power to
  other devices.                                                              
                                                                              
  Then, the functions  connect_to_wifi  and  get_ip_address  are called by    
  using the SSID and password from  secret  module. This code will establish a
  Wi-Fi connection.                                                           
                                                                              
    connect_to_wifi(ssid, password)                                           
    ip = get_ip_address()                                                     
                                                                              
  Now that the Wi-Fi connection is established, routes are set for the server:
                                                                              
    @server.route("/led", methods=["GET"])                                    
    def led_toggle(request):                                                  
        led.toggle()                                                          
        return f"{led.value()}"                                               
                                                                              
  This function responds to GET requests to "/led" path and toggles the LED.  
  It returns a string representing the current state of LED.  led.toggle()  is
  a function to change the state of the LED from ON to OFF or from OFF to ON. 
  led.value()  is a function to get the current state of the LED.             
                                                                              
  This function catches all requests to paths other than "/led" and returns a 
  404 error:                                                                  
                                                                              
    @server.catchall()                                                        
    def catchall(request):                                                    
        return "Not found", 404                                               
                                                                              
  Finally, the server is started with the  server.run()  command. The server  
  will now continuously listen for incoming requests until it is manually     
  stopped.                                                                    
                                                                              
    server.run()

## Documentation

For more information, please refer to the following links:

1. MicroPython Documentation: [https://docs.micropython.org/en/latest/](https://docs.micropython.org/en/latest/)
2. Thonny Documentation: [https://thonny.org/help/](https://thonny.org/help/)
3. Phew Documentation: [https://github.com/pimoroni/phew](https://github.com/pimoroni/phew)

In case you encounter issues or need further assistance, please refer to the documentation first.

