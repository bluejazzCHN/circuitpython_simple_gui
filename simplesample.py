import board
import time
import displayio
import adafruit_displayio_ssd1306
import random

from circuitpython_simple_gui import GUI


displayio.release_displays()

WIDTH = 128
HEIGHT = 64

i2c = board.I2C()  # uses board.SCL and board.SDA
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

sens_number =3
sens_names = ["Temp","Humi","Pres"]
sens_values = ["","",""]

gui = GUI(display,head_name="SIMPLE UI",name_list=sens_names,value_list=sens_values,numbers=sens_number)

while True:
    time.sleep(10)
    gui.set_main(["{:.1f}".format(random.random()*40),"{:.1f}".format(random.random()*100),"{:.0f}".format((random.random()+1)*1000)])





































