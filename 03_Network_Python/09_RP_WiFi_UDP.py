import network
import usocket as socket
import time
import uselect as select
import machine


led_onboard = machine.Pin('LED', machine.Pin.OUT)
ssid = "DDTSW_Classroom_1"
password = "11111111"

client_port = 23

server_ip = "192.168.1.211"
server_port = 12345

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

def main():
    cnt = 0
    if wifi_connect():
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.bind(('0.0.0.0', client_port))

        try:
            server_addr = (server_ip, server_port)
            inputs = [client_socket]
            print("Connected to server")

            while True:
                cnt += 1
                data_to_send = f"Hello, Server! [{cnt}]"
                client_socket.sendto(data_to_send.encode('utf-8'), server_addr)
                print("Sent data:", data_to_send)

                readable, _, _ = select.select(inputs, [], [], 1)
                for sock in readable:
                    data_received, addr = sock.recvfrom(1024)
                    if data_received:
                        print("Received data:", data_received.decode('utf-8'))

        except Exception as e:
            print("Error:", e)
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
