import network # type: ignore
from microdot import Microdot, Response # type: ignore
import time

ssid = ''
password = ''

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig(('192.168.1.111','255.255.255.0','192.168.1.1','8.8.8.8'))
wlan.connect(ssid, password)

while not wlan.isconnected():
    print('Connecting to WiFi...')
    time.sleep(1)

app = Microdot()

@app.route('/')
def index(request):
    return 'Hello from ESP32 Server!'

@app.route('/data', methods=['POST'])
def data(request):
    data = request.json
    print('Received data:', data)
    return Response('Data received', status=200)

app.run(host='0.0.0.0', port=80)