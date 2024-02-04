from secrets import ssid, password
import network
from time import sleep
from machine import Pin
import requests
import mip

led = Pin("LED", Pin.OUT)
led.value(0)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

if not wlan.isconnected:
    led.toggle()
    sleep(0.1)
if wlan.isconnected:
    led.toggle()
    print(wlan.ifconfig())
    print("wifi connected")
    print(requests.get("https://google.com"))


led.value(0)
mip.install("github:pimoroni/phew")
