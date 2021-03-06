import machine
import time

import ssd1306
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
# import machine
# import ssd1306
# spi = machine.SPI(1, baudrate=8000000, polarity=0, phase=0)
# oled = ssd1306.SSD1306_SPI(128, 32, spi, machine.Pin(4), machine.Pin(16), machine.Pin(15))

pin = machine.Pin(2, machine.Pin.OUT)

#oled.fill(1)
oled.text("  Feliz Navidad ", 0, 0)
oled.text("     Pronet     ", 0, 10)
oled.text("   Technology   ", 0, 20)
oled.show()

def toggle(p):
    p.value(not p.value())
    oled.invert(False if (p.value() == 0) else True)

while True:
    toggle(pin)
    time.sleep_ms(300)
