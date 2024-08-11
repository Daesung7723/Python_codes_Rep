import paho.mqtt.publish as publish
from tkinter import *

broker = "192.168.1.211"

def change_color():
    global button_bg, button_txt
    
    if button_bg == 'blue':
        button_bg='red'
        button_txt = 'ON'
    else:
        button_bg = 'blue'
        button_txt = 'OFF'
        
    button.configure(text = button_txt, bg=button_bg)
    publish.single("/RP_Pico", button_txt, hostname=broker)
    
root = Tk()
button_bg='blue'
button_txt = 'OFF'

button = Button(root, text = button_txt, fg='yellow',
                font = ('Vernada', 30), bg=button_bg, command = change_color)
button.pack()
root.mainloop()