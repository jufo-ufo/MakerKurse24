from lcd_i2c import LCD
from machine import I2C, Pin

i2c = i2c = I2C(0)

print(i2c.scan())

I2C_ADDR = 0x27 # 39 
lcd = LCD(addr=I2C_ADDR, cols=16, rows=2, i2c=i2c)

lcd.begin()
lcd.print("Hello World")

