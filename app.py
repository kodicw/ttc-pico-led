from secret import ssid, password
from phew import server, connect_to_wifi, get_ip_address
from machine import Pin
led = Pin("LED", Pin.OUT)

connect_to_wifi(ssid, password)
ip = get_ip_address()
@server.route("/random", methods=["GET"])
def random_number(request):
  import random
  min = int(request.query.get("min", 0))
  max = int(request.query.get("max", 100))
  return str(random.randint(min, max))

@server.route("/led", methods=["GET"])
def led_toggle(request):
    led.toggle()
    return f"{led.value()}"

@server.route("/", methods=["GET"])
def led_toggle(request):
    return f"""
  <script src="https://unpkg.com/htmx.org@1.9.10"></script>
  <!-- have a button POST a click via AJAX -->
  <button hx-get="/led" hx-trigger"every 1sec">
    Click Me
  </button>"""
    
@server.catchall()
def catchall(request):
  return "Not found", 404

server.run()
