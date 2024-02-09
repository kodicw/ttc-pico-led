from secret import ssid, password
from phew import server, connect_to_wifi, get_ip_address
from machine import Pin
import time

led = Pin("LED", Pin.OUT)

connect_to_wifi(ssid, password)
ip = get_ip_address()


print(ip)
@server.route("/", methods=["GET"])
def index_html(request):
    with open("index.html") as f:
        base_html = f.read()
    return base_html


@server.route("/led", methods=["GET"])
def led_toggle(request):
     led.toggle()
     if led.value():
         return "Blink"
     return "Blonk"


# This will catch all other paths and return a 404
@server.catchall()
def catchall(request):
    return "Not found", 404


server.run()

