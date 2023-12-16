# SPDX-FileCopyrightText: Copyright (c) 2023 Songjiang Zhang
#
# SPDX-License-Identifier: MIT

"""
Quickly build your UI in mcu for circuitpython

Features:
    - Very simple api to call
    - Very lightweight and no external dependencies.
    - simplest ui is comprised with header, main and trail.  main is used to diaplsy value of sensor, trail is used to dispaly name of sensor.

Usage:
    >>> import board
    >>> import time
    >>> import displayio
    >>> import adafruit_displayio_ssd1306
    >>> import random
    >>> from gui import GUI
    >>>
    >>> displayio.release_displays()

    >>> WIDTH = 128
    >>> HEIGHT = 64

    >>> i2c = board.I2C()  # uses board.SCL and board.SDA
    >>> display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

    >>> display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)
        
        #build a weather station to display tempreture , humility, pressure sensor data only two core code.
    >>> sens_number =3
    >>> sens_names = ["Temp","Humi","Pres"]
    >>> sens_values = ["","",""]
    
        #UI class init
    >>> gui = GUI(display,head_name="SIMPLE UI",name_list=sens_names,value_list=sens_values,numbers=sens_number)

    >>> while True:
    >>>    time.sleep(10)
    
        #update sensor data
    >>>    gui.set_main(["{:.1f}".format(random.random()*40),"{:.1f}".format(random.random()*100),"{:.0f}".format((random.random()+1)*1000)])
    
"""
import terminalio
from adafruit_display_text import label
import displayio
from adafruit_bitmap_font import bitmap_font

    
class GUI:
    
    def __init__(self,display,head_name="GUI STATION",name_list=["Waiting","Waiting"],value_list=["",""],numbers =2) -> None:
        self._display = display
        self._name_list = name_list
        self._value_list = value_list
        self._head_group = None
        self._trail_group = None
        self._main_group = None
        self._display_group = displayio.Group()
        self._display.root_group =self._display_group
        
        self._head_name = None
        self._head_font = None
        self._head_color = None
        self._head_area = None

        self._trail_area = displayio.Group()
        self._trail_font = None
        self._trial_color = 0xffffff
        
        self._main_area = displayio.Group()
        self._main_font = None
        self._main_color = 0xffffff
        
        self._head_group_init(text=head_name)
        self._main_group_init(numbers = numbers)
        self._trail_group_init(numbers = numbers)
    
    def show_display(self):
        _display.refresh()
    
    def _head_group_init(self,text = "GUI STATION",color = 0xffffff, font = terminalio.FONT):
        self._head_name = text        
        self._head_font = font
        self._head_color = color
        self._head_area = label.Label(self._head_font,text=self._head_name,color=self._head_color)
        self._head_area.anchor_point =(0.5,0.5)
        self._head_area.anchored_position =(64,10)
        self._display_group.append(self._head_area)
        print("head init finished")
        
    
    def _trail_group_init(self,color = 0xffffff, font = terminalio.FONT,numbers=2):
        self._trail_text = self._name_list
        self._trail_font = font
        self._trail_color = color
        x = self._display.width/numbers
        y = self._display.height/numbers
        
        for i in range(numbers):
            temp_label = label.Label(self._trail_font,text=self._trail_text[i],color=self._trail_color)
            temp_label.anchor_point =(0.5,0.5)
            temp_label.anchored_position =(x/2+x*i,56)
            self._trail_area.append(temp_label)
            
        self._display_group.append(self._trail_area)
        print("trail init finished")
    
    def _main_group_init(self,color = 0xffffff, font = bitmap_font.load_font("/Helvetica-Bold-16.bdf"),numbers = 2): 
        self._main_text = self._value_list
        self._main_font = font
        self._main_color = color
        x = self._display.width/numbers
        y = self._display.height/numbers
        
        for i in range(numbers):
            temp_label = label.Label(self._main_font,text=self._main_text[i],color=self._main_color)
            temp_label.anchor_point =(0.5,0.5)
            temp_label.anchored_position =(x/2+x*i,32)
            self._main_area.append(temp_label)

        self._display_group.append(self._main_area)
        print("main init finished")
        
    def set_head(self,text):
        self._head_area.text = text
    
    def set_trail(self,name_list):
        self._name_list = name_list
        for i in range(len(self._main_area)):
            self._trail_area[i].text = self._name_list[i]
        
    def set_main(self,value_list):
        self._value_list = value_list
        for i in range(len(self._main_area)):
            self._main_area[i].text = self._value_list[i]