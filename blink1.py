from secret import ssid, password
from phew import server, connect_to_wifi, get_ip_address
from machine import Pin

led = Pin("LED", Pin.OUT)

connect_to_wifi(ssid, password)
ip = get_ip_address()


@server.route("/led", methods=["GET"])
def led_toggle(request):
    led.toggle()
    return f"{led.value()}"


# This will catch all other paths and return a 404
@server.catchall()
def catchall(request):
    return "Not found", 404


server.run()
