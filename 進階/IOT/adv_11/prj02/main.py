import time
import mcu


gpio = mcu.gpio()
servo = mcu.servo(gpio.D8)
servo.angle(180)
time.sleep(1)
servo.angle(90)
time.sleep(1)
