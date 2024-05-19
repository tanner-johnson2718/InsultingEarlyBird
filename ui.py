from RPLCD.i2c import CharLCD

lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=20, rows=4, dotsize=8)

menu = ["Pos) ", "Time) ", "Alarm) ", "State) "]
state= ["Pending", "Descending", "Ascending"]

lcd.clear()
for s in menu:
    pad = ' ' * (20 - len(s)) 
    lcd.write_string(s + pad)