import time
import network
from mqtt import MQTTClient
import machine


led_onboard = machine.Pin('LED', machine.Pin.OUT)

ssid = "DDTSW_Classroom_1"
password = "11111111"

broker = "192.168.1.211"
PORT=1883
CLIENT_ID="RP_Pico" 
PUB_TOPIC="/pc"
cnt = 0

def wifi_disconnect():
    wlan = network.WLAN(network.STA_IF)
    if wlan.isconnected():
        print("Disconnecting from network...")
        wlan.disconnect()
        while wlan.isconnected():
            led_onboard.toggle()
            time.sleep_ms(100)
        print("Disconnected from network")
        led_onboard.value(0)

def wifi_connect():
    wlan = network.WLAN(network.STA_IF) 
    wlan.active(True) 

    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)  

        while not wlan.isconnected():
            led_onboard.toggle()
            time.sleep_ms(100)

        print(f"Connected to {ssid} successfully!")
        print('Network Config :', wlan.ifconfig())
        led_onboard.value(1)
        return True
    else:
        print("Already connected to network:", wlan.ifconfig())
        return True


if __name__=="__main__":
    wifi_disconnect()
    if wifi_connect():
        client = MQTTClient(CLIENT_ID, broker, PORT)
        client.connect()
        
        while True:
            cnt = cnt+1
            client.publish(PUB_TOPIC, f"Hello pc : {cnt}")
            time.sleep(1.0)
