from microbit import *
from lcd_i2c import LCD1602  # 請確保你有這個模組
import sys

# 腳位設定
TEMP_PIN = pin2  # 溫度感測器
GAS_PIN = pin1  # 氣體感測器
PIR_PIN = pin15  # 人體紅外線感測器
LED_PIN = pin16  # 照明 LED
RGB_PIN = pin14  # RGB 或警示 LED
FAN_PIN = pin0  # 風扇控制腳位

# 系統設定
TEMP_THRESHOLD = 30  # 溫度閾值
GAS_THRESHOLD = 500  # 氣體閾值
UPDATE_INTERVAL = 100  # 更新間隔 (ms)

# 感測值
temperature = 0
gas_value = 0
pir_detected = False


def init_system():
    """初始化 LCD 與感測器"""
    try:
        lcd = LCD1602(0x27)
        lcd.clear()
        lcd.putstr("System Init...")
        read_sensors()
        return lcd
    except Exception as e:
        print("LCD 初始化錯誤:", e)
        sys.exit(1)


def read_sensors():
    global temperature, gas_value, pir_detected
    try:
        temperature = TEMP_PIN.read_analog() * 50 / 1023  # 模擬轉攝氏
        gas_value = GAS_PIN.read_analog()
        pir_detected = PIR_PIN.read_digital()
    except Exception as e:
        print("讀取感測器錯誤:", e)


def update_display(lcd):
    try:
        lcd.clear()
        lcd.move_to(0, 0)
        lcd.putstr(f"T:{round(temperature,1)}C G:{gas_value}")
        lcd.move_to(0, 1)
        status = "Move" if pir_detected else "Still"
        lcd.putstr(f"Status:{status}")
    except Exception as e:
        print("LCD 顯示錯誤:", e)


def control_devices(lcd):
    try:
        over_temp = temperature > TEMP_THRESHOLD
        over_gas = gas_value > GAS_THRESHOLD

        # 溫度或氣體過高警示燈
        if over_temp or over_gas:
            RGB_PIN.write_digital(1)
        else:
            RGB_PIN.write_digital(0)

        # 人體移動 -> 開燈
        if pir_detected:
            LED_PIN.write_digital(1)
        else:
            LED_PIN.write_digital(0)

        # 溫度過高 -> 開風扇
        if over_temp:
            FAN_PIN.write_digital(1)
        else:
            FAN_PIN.write_digital(0)

    except Exception as e:
        print("裝置控制錯誤:", e)


def main():
    lcd = init_system()
    while True:
        try:
            read_sensors()
            update_display(lcd)
            control_devices(lcd)
            pause(UPDATE_INTERVAL)
        except Exception as e:
            print("主程式錯誤:", e)
            RGB_PIN.write_digital(1)
            pause(500)
            RGB_PIN.write_digital(0)
            pause(500)


if __name__ == "__main__":
    main()
