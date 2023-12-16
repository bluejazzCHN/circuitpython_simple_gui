# CircuitPython Simple GUI

### Quickly build your UI in mcu for circuitpython

### Features:
    - Very simple api to call
    - Very lightweight and no external dependencies.
    - simplest ui is comprised with header, main and trail.  main is used to diaplsy value of sensor, trail is used to dispaly name of sensor.

### Usage:

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
    
    #build a weather station to display tempreture , humility, pressure sensor data 
    #only two essential code.
    sens_number =3
    sens_names = ["Temp","Humi","Pres"]
    sens_values = ["","",""]
    
    #UI class init -- first line
    gui = GUI(display,head_name="SIMPLE UI",name_list=sens_names,value_list=sens_values,numbers=sens_number)
    while True:
       time.sleep(10)
       #update sensor data --second line
       gui.set_main(["{:.1f}".format(random.random()*40),"{:.1f}".format(random.random()*100),"{:.0f}".format((random.random()+1)*1000)])
