import time
import network
from mqtt import MQTTClient
from machine import Pin, Timer

led_onboard = Pin('LED', Pin.OUT)

ssid = "N-517"
password = "83634038"
ssid = "DDTSW_Classroom_1"
password = "11111111"

SERVER = "192.168.1.211"
PORT=1883
CLIENT_ID="RP_Pico" 
PUB_TOPIC="/pc"
SUB_TOPIC = "/RP_Pico"

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


def sub_callback(topic, msg):
    print("Data Subscribe..")
    print(topic, msg)


def mqtt_send(tim):
    client.publish(PUB_TOPIC, "Hello pc from RP_Pico")


if __name__=="__main__":
    if wifi_connect():
        client = MQTTClient(CLIENT_ID, SERVER, PORT)
        client.set_callback(sub_callback)
        client.connect()
        client.subscribe(SUB_TOPIC)
        
        tim = Timer(mode=Timer.PERIODIC, period=1000, callback=mqtt_send)
        
        while True:
            client.check_msg()
