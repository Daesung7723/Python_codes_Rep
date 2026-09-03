import paho.mqtt.subscribe as subscribe
from tkinter import *

def Receiving():
    topics = "/pc"
    broker = "192.168.1.211"
    m=subscribe.simple(topics, hostname=broker, msg_count=1)
    entry.delete(0, END)
    entry.insert(1, m.payload.decode('utf-8'))

def polling():
    Receiving()
    root.after(500, polling)

root = Tk()
label1 = Label(root, font=('Verdana', 30), text="Recv. Msg")
label1.grid(row=0, column=0)
entry = Entry(font=('Verdana', 30), width=50)
entry.grid(row=0, column=1)

#Receiving()
print("Waiting for message")
print("Run the message publishing program")
polling()
mainloop()
