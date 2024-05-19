from RPLCD.i2c import CharLCD
import time
from datetime import datetime

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)

menu = ["Pos)   ", "Time)  ", "Alarm) ", "State) "]
state= ["Pending", "Descending", "Ascending"]

def get_pos():
    return 0

def update_menu():
    c = datetime.now()

    menu[0] = "Pos   ) " +  str(get_pos(0))
    menu[1] = "Time  ) " + c.strftime('%H:%M:%S')
    menu[2] = "Alarm ) " + "OFF"
    menu[3] = "State ) " + "OFF"

while 1:
    time.sleep(1)
    lcd.clear()
    for s in menu:
        pad = ' ' * (20 - len(s)) 
        lcd.write_string(s + pad)