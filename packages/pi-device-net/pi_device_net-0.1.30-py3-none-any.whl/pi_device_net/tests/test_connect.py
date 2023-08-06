# test_connect.py
import socket

import paho.mqtt.client as mqtt

# The callback function. It will be triggered when trying to connect to the MQTT broker
# client is the client instance connected this time
# userdata is users' information, usually empty. If it is needed, you can set it through user_data_set function.
# flags save the dictionary of broker response flag.
# rc is the response code.
# Generally, we only need to pay attention to whether the response code is 0.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected success")
    else:
        print(f"Connected fail with code {rc}")

def discover_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(("10.255.255.255", 1))
        ip = sock.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        sock.close()
    return ip

client = mqtt.Client()
client.on_connect = on_connect
ip = discover_ip()
print(f"Local IP: {ip}")

print("Connect 0")
client.connect("magic")

# print("Connect 1")
# client.connect(ip, 1883, 60)

# print("Connect 2")
# client.connect(ip)

# print("Connect 3")
# client.connect("broker.emqx.io", 1883, 60)

# print("Connect 4")
# client.connect("localhost", 1883, 60)

client.loop_forever()