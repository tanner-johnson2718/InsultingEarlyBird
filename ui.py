from RPLCD.i2c import CharLCD
import time
from datetime import datetime
import os

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)

menu = ["Pos)   ", "Time)  ", "Alarm) ", "State) "]
states= ["Pending", "Descending", "Ascending"]
os.environ['TZ'] = 'America/Denver'
time.tzset()
alarm = "05:30:00"
pos = 0
pos_prev = 0

state_index = 0
state=states[0]

def state_next():
    state_index = ((state_index+1) % len(states))
    state= states[state_index]

def get_pos():
    return 0

def rise_n_shine(date_string):
    alarm_split = alarm.split(':')
    time_split = date_string.split(':')

    hour_equal = (alarm_split[0] == time_split[0])
    minute_equal = (alarm_split[1] == time_split[1])
    second_greater = (alarm_split[2] >= time_split[2])

    return hour_equal and minute_equal and second_greater

def send_ascend():
    return 0

def send_descend():
    return 0

def update():
    c = datetime.now()
    date_string = c.strftime('%H:%M:%S')
    pos = get_pos()

    if state == states[0]:
        if rise_n_shine(date_string):
            lcd.clear()
            menu[0] = "Pos   ) " +  str(pos)
            menu[1] = "Time  ) " + date_string
            menu[2] = "Alarm ) " + alarm
            menu[3] = "State ) " + "Triggered"
            time.sleep(60)
            send_descend()
            state_next()
    elif state == states[1]:
        if pos == pos_prev:
            send_ascend()
            state_next()
    elif state == states[2]:
        if pos == pos_prev:
            state_next()
            
    lcd.clear()
    menu[0] = "Pos   ) " +  str(pos)
    menu[1] = "Time  ) " + date_string
    menu[2] = "Alarm ) " + alarm
    menu[3] = "State ) " + state

while 1:
    update()
    lcd.clear()
    for s in menu:
        pad = ' ' * (20 - len(s)) 
        lcd.write_string(s + pad)
    time.sleep(7)